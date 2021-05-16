from typing import Callable, Tuple, Union, Literal
from collections import defaultdict

from numpy import float64, longdouble, sum as np_sum, array as np_array, zeros as np_zeros, ceil as np_ceil, append as np_append
from numpy.random import binomial as binomial_experiment
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.ticker as ticker
from tqdm.std import trange

from lib.math_functions import binomial_distribution_pmf, binomial_distribution_two_tailed_range, get_binomial_z_precision, normal_z_score_two_tailed
from lib.data_functions import float_to_str, precise_float_diff
from lib.CI_efficacy import NoCoverageException, plot_styles
from lib.CI_efficacy_proportion import CImethodForProportion_efficacyToolkit, CImethodForProportion_efficacyToolkit_format, proportions_type



CI_method_for_diff_betw_two_proportions = Callable[
    [int, int, int, int, Union[float, None], Union[float, None]],
    Tuple[float, float]
]


class CImethodForDiffBetwTwoProportions_efficacyToolkit_format(CImethodForProportion_efficacyToolkit_format):
    def __init__(self, efficacy_toolkit):
        self.efficacy_toolkit: CImethodForDiffBetwTwoProportions_efficacyToolkit = efficacy_toolkit

    def calculation_inputs(self):
        printed_inputs = (
            f"CI_method = '{self.efficacy_toolkit.method_name}', confidence = {float_to_str(self.efficacy_toolkit.confidence*100)}%,\n"
            f"n1 = {self.efficacy_toolkit.sample_size1}, n2 = {self.efficacy_toolkit.sample_size2}\n"
            f"ps[{len(self.efficacy_toolkit.proportions)}] = ({self.efficacy_toolkit.proportions[0]}...{self.efficacy_toolkit.proportions[-1]},d={precise_float_diff(self.efficacy_toolkit.proportions[1], self.efficacy_toolkit.proportions[0])})"
        )
        return printed_inputs


class CImethodForDiffBetwTwoProportions_efficacyToolkit(CImethodForProportion_efficacyToolkit):
    """A toolkit for studying efficacy of a CI method for the difference between two proportions.

    Parameters
    ----------
    method : CI_method
        a studied method for calculating CI for the difference between two proportions

    method_name : str
        a human-readable name of the method.

    Attributes
    ----------
    method : CI_method
        a studied method for calculating CI for the difference between two proportions

    method_name : str
        a human-readable name of the method.

    confidence : float
        A number between 0 and 1.
        Confidence interval - coverage that you want to get
        (see frequentist definition of confidence interval).

    sample_size1 : int
        Number of trials in the first sample

    sample_size2 : int
        Number of trials in the second sample

    proportions : List[np.float64]
        A list of true proportions to try.

    coverage : np.ndarray
        2d array, np.longdouble, values between 0 and 100
        Coverage represents a proportion of cases that fall under the confidence interval produced
        by the given `method` for a particular case of two proportions from the given list.
        User can assess the efficacy of a CI method by comparing these values to the `confidence`.
         - Values `< confidence` mean the `method` is more likely to cause a type I error.
         In simple words, this is bad because you would not be able say
         you are `confidence*100`% confident that the true population proportion
         lies within the interval calculated by the `method`.
         - Values `> confidence` mean the `method` is even less likely to cause a type I error,
         but may be more likely to cause a type II error.
         In simple words, it doesn't necessarily mean the `method` is bad, but it's
         just "concervative". Whether it is way too concenrvative or not is up to you.
         If you pass `0.95` (95%) to the `method`, and it gives you 99.5% coverage, 
         it is hell of a concervative method.

    average_coverage : np.longdouble
        average of all values in `coverage`

    average_deviation : np.longdouble
        average deviation of all values in `coverage` from `confidence`

    f : CImethodForDiffBetwTwoProportions_efficacyToolkit_format
        Formatting helper. See the class

    figure : matplotlib.figure.Figure
        a matplotlib figure that's being generated by plotting the `coverage`

    """

    def __init__(self, method: CI_method_for_diff_betw_two_proportions, method_name: str):
        self._method: CI_method_for_diff_betw_two_proportions = method
        self._method_name: str = method_name

        self._f = CImethodForDiffBetwTwoProportions_efficacyToolkit_format(self)


    @property
    def sample_size1(self):
        return self._sample_size1

    @sample_size1.setter
    def sample_size1(self, value: int):
        if not value > 0: raise ValueError(
            f"sample size has to be greater than 0. Got: sample_size1={value}")
        self._sample_size1 = value


    @property
    def sample_size2(self):
        return self._sample_size2

    @sample_size2.setter
    def sample_size2(self, value: int):
        if not value > 0: raise ValueError(
            f"sample size has to be greater than 0. Got: sample_size2={value}")
        self._sample_size2 = value


    @property
    def f(self) -> CImethodForDiffBetwTwoProportions_efficacyToolkit_format:
        return self._f


    def calculate_coverage_randomly(self,
            sample_size1: int,
            sample_size2: int,
            proportions: proportions_type,
            confidence: float,
            n_of_experiments: int = 10000
            ):
        """
        Calculates true coverage of confidence interval for the difference between two proportions
        produced by the `method` for the given desired `confidence` using a simulation
        with a number of random experiments (`n_of_experiments`).

        Number of trials for both samples are `sample_size1` and `sample_size2`.

        Two proportions for samples 1 and 2 are taken from the list `proportions`,
        each against each, producing 2d square matrix of results,
        a value for each pair of proportions.

        This 2d square matrix is `coverage`, and is saved to `self.coverage`.
        """
        self.confidence = confidence
        self.proportions = self.form_proportions_list(proportions)
        self.sample_size1 = sample_size1
        self.sample_size2 = sample_size2

        if __debug__ is True:
            print(
                self.f.calculation_inputs() + ",\n"
                f"calculation_method = random simulation, " +
                f"n_of_experiments = {n_of_experiments}"
            )

        # n by n zero matrix, where n is the number of tested probabilities (actual population proportions)
        coverage = np_zeros((len(self.proportions),len(self.proportions)), dtype=longdouble)

        # The return value of this function will be cached (this is not necessary)
        z = normal_z_score_two_tailed(p=confidence)

        progress_bar_str = "p1={}; p2={} => cov={}%"
        """
        Here we loop through the cartesian square of the list `self.proportions`,
        (cartesian product of the list `self.proportions` with itself)

        But there's no need to loop through the entire "matrix":
        for each pair `(xi, xj)` the same result can be used for `(xj, xi)`.
        Therefore, only "left diagonal matrix" elements of this "matrix" have to be included
        """
        t = trange(len(self.proportions),
                   desc=progress_bar_str.format("***","***","***"))
        for i in t:
            for j in range(i, len(self.proportions)):
                (prob_x1, prob_x2) = self.proportions[i], self.proportions[j]
                delta = abs(prob_x2 - prob_x1)
                x1 = binomial_experiment(sample_size1, prob_x1, n_of_experiments)
                x2 = binomial_experiment(sample_size2, prob_x2, n_of_experiments)

                CIs = [self.method(x1[k], sample_size1, x2[k], sample_size2, confidence)
                                                    for k in range(0, n_of_experiments)]
                covered = [int(CI[0] < delta < CI[1]) for CI in CIs]

                # multiplied by 100 in-place for better progress bar, and for a better figure later
                thiscoverage = (sum(covered)/n_of_experiments) * 100

                coverage[i][j] = coverage[j][i] = thiscoverage

                t.set_description(progress_bar_str.format(
                    self.f.proportion(prob_x1), self.f.proportion(prob_x2),
                    self.f.coverage(thiscoverage)))

        self.coverage = coverage
        t.set_description(progress_bar_str.format(
            "*", "*", self.f.coverage(self.average_coverage)))
        print(f"average confidence level {self.f.coverage(self.average_coverage)}")
        print(f"average deviation from {self.f.confidence_percent} = {self.f.coverage(self.average_deviation)} (coverage %)")
        print("")
        return self.coverage


    def calculate_coverage_analytically(self,
            sample_size1: int,
            sample_size2: int,
            proportions: proportions_type,
            confidence: float,
            z_precision: Union[float, Literal['auto']] = 'auto'
            ):
        """
        Calculates true coverage of confidence interval for the difference between two proportions
        produced by the `method` for the given desired `confidence` using
        an indistinguishably precise approximation for the analytical solution.

        Optimal approximation precision is auto-picked for the specific case,
        but can be set manually in `z_precision`. This is a z-value for precision instead of p.
        Meaning, `z_precision` of 1.96 is 95% precision (which is a terrible precision).

        Number of trials for both samples are `sample_size1` and `sample_size2`.

        Two proportions for samples 1 and 2 are taken from the list `proportions`,
        each against each, producing 2d square matrix of results,
        a value for each pair of proportions.

        This 2d square matrix is `coverage`, and is saved to `self.coverage`.
        """
        self.confidence = confidence
        self.proportions = self.form_proportions_list(proportions)
        self.sample_size1 = sample_size1
        self.sample_size2 = sample_size2

        if z_precision == 'auto':
            z_precision = get_binomial_z_precision(confidence)

        if __debug__ is True:
            print(
                self.f.calculation_inputs() + ",\n"
                f"calculation_method = analytical approximation, " +
                f"z_precision = {z_precision:5.2f}"
            )

        # `n` by `n` 0-matrix, where `n` - the number of probabilities (population proportions)
        coverage = np_zeros((len(self.proportions),len(self.proportions)), dtype=longdouble)

        progress_bar_str = "p1={}; p2={} => cov={}%"
        """
        Here we loop through the cartesian square of the list `self.proportions`,
        (cartesian product of the list `self.proportions` with itself)

        But there's no need to loop through the entire "matrix":
        for each pair `(xi, xj)` the same result can be used for `(xj, xi)`.
        Therefore, only "left diagonal matrix" elements of this "matrix" have to be included
        """
        t = trange(len(self.proportions),
                   desc=progress_bar_str.format("***","***","***"))
        for i in t:
            for j in range(i, len(self.proportions)):
                (prob_x1, prob_x2) = self.proportions[i], self.proportions[j]
                delta = abs(prob_x2 - prob_x1)

                """The entire range of the binomial distribution could be used"""
                #x1_from, x1_to = (0, sample_size)
                #x2_from, x2_to = (0, sample_size)
                """
                This is too computationally expensive to calculate CI for `y` value of each `x1`
                and `x2` of a 2-variate binomial distribution.
                Since most `y` values of the binomial distribution are very close to zero,
                we can use only a small part of the binomial distribution around the peak.
                Such part of a binomial distribution can often be efficiently modeled
                with a normal distribution.

                Let's say we need to consider the span covering 99.999% percent of the mass
                of the two-variate binomial distribution. According to the normal distribution,
                this would be a range that spans 4.42 standard deviations from the mean on both
                sides for both single-variate binomial distribution from which the two-variate one
                is constructed. 
                The span of 4.42 sigma would cover around 99.999% of a binomial distribution
                `Binom(n,p)` for most values of `n` and `p`. This would nail it for 95%CI, but
                what if a user wants to ask for 99.999%CI, and we are only considering 99.999%
                of the binomial distribution? We'd need to consider much more expansive range
                in our calculations.

                We would need something like this:
                for 95% confidence         => 99.995%         of the distribution (4.056 sigma)
                for 99% confidence         => 99.999%         of the distribution (4.417 sigma)
                for 99.9% confidence       => 99.9999%        of the distribution (4.892 sigma)
                for 99.99% confidence      => 99.999_99%      of the distribution (5.327 sigma)
                for significant range of 5 sigma:
                for 99.999_943% confidence => 99.999_999_943% of the distribution (6.199 sigma)
                etc.

                Thus, precision is to be determined given the `confidence`. A specific formula
                is used to figure out the optimal `z_precision`.
                """
                x1_from, x1_to = binomial_distribution_two_tailed_range(n=sample_size1, p=prob_x1, sds=z_precision)
                x2_from, x2_to = binomial_distribution_two_tailed_range(n=sample_size2, p=prob_x2, sds=z_precision)
                x1s = range(x1_from, x1_to+1)
                x2s = range(x2_from, x2_to+1)

                CIs = [[
                    self.method(x1, self.sample_size1, x2, self.sample_size2, self.confidence)
                        for x2 in x2s] for x1 in x1s]

                # Array of `1`s and `0`s
                # int constructor could be used, but longdouble is used to provide better precision
                covered = [[longdouble(CIs[i1][i2][0] < delta < CIs[i1][i2][1])
                                                 for i2 in range(len(CIs[i1]))]
                                                         for i1 in range(len(CIs))]

                # multiplied by 100 in-place for better progress bar, and for a better figure later
                thiscoverage = 100 * (np_sum(
                    [covered[i][j] *
                     binomial_distribution_pmf(x1s[i], sample_size1, prob_x1) *
                     binomial_distribution_pmf(x2s[j], sample_size2, prob_x2)
                         for i in range(len(x1s)) for j in range(len(x2s))]
                ))

                coverage[i][j] = coverage[j][i] = thiscoverage
                t.set_description(progress_bar_str.format(
                    self.f.proportion(prob_x1), self.f.proportion(prob_x2),
                    self.f.coverage(thiscoverage)))

        self.coverage = coverage
        t.set_description(progress_bar_str.format(
            "*", "*", self.f.coverage(self.average_coverage)))
        print(f"average confidence level {self.f.coverage(self.average_coverage)}")
        print(f"average deviation from {self.f.confidence_percent} = {self.f.coverage(self.average_deviation)} (coverage %)")
        print("")
        return self.coverage


    def plot_coverage(self,
            plt_figure_title: str,
            title: str = "Coverage of {method_name}\nsamples: n1 = {sample_size1}, n2 = {sample_size2}",
            theme: plot_styles = "default",
            colors: Tuple[str,str,str,str,str] = ("gray", "purple", "white", "#b8df96", "green")
            ):
        """
        Plots the `matplotlib.pyplot` figure given the data from previous coverage calculation and
        some captions and formatting.
        """
        if self.coverage is None: raise NoCoverageException(
            "you have to calculate coverage first before plotting it")

        # this unpacked defaultdict trouble allows for optional formatting placeholders
        title = title.format(**defaultdict(str, 
            method_name  = self.method_name,
            sample_size1 = self.sample_size1,
            sample_size2 = self.sample_size2
        ))


        plt.style.use(theme)

        """
        Colorbar range depends on confidence level.
        Sets vmin to a point 10 times farther from 100% than the confidence

        for confidence=95% show colorbar from 50% to 100%;
        for confidence=99% show colorbar from 90% to 100%;
        for confidence=99.9% show colorbar from 99% to 100%;
        """
        vmin = 100 - ( (100-(self.confidence*100))*10 )
        vmax = 100

        """
        In LinearSegmentedColormap specified color points have to span from 0 to 1,
        where 0 would correspond to vmin, and 1 to vmax.

        the 5 specified colors will form a gradient by marking at points below.
        For confidence=95%: (50, 90, 95, 97.5, 100)
        For confidence=99%: (90, 98, 99, 99.5, 100)

        But because the following value is constant, visually, the colorbar itself will always have
        the same gradient regardless of the given `confidence` value
        """
        nodes = (0.0, 0.8, 0.9, 0.95, 1.0)

        cmap = LinearSegmentedColormap.from_list("", list(zip(nodes, colors)))
        cmap.set_under(colors[0])

        fig, ax = plt.subplots()
        fig.canvas.set_window_title(plt_figure_title)

        """
        Would be great if matplotlib supported float128/longdouble. Instead, it converts data
        to float64 with a warning:
            "UserWarning: Casting input data from 'float128' to 'float64' for imshow"

        But!
        float128 precision could possible be utilized while using float64 in this case.
        If we were to display not the value (the coverage, 0-100), but the difference between
        the expected coverage (confidence) and the actual coverage, float64 would do a lot better.
        This can be done, but some adjustments have to be made to colorbar and labels.
        """
        im = ax.imshow(float64(np_array(self.coverage)),
            cmap=cmap,
            norm=Normalize(float(vmin), vmax, True)
        )

        # precision of "8" decimal places should be more than enough for colorbar ticks
        cb = fig.colorbar(im, format=ticker.FuncFormatter(lambda x, pos: (f'%.8f' % x).rstrip('0').rstrip('.')))
        # plot a dashed black line over *confidence* point on a colorbar
        cb.ax.plot([0, 100], [self.confidence*100, self.confidence*100], '_:k')

        # rewriting autogenerated colorbar ticks by adding one that corresponds to `confidence`
        colorbar_ticks = cb.ax.get_yticks()
        colorbar_ticks = np_append(colorbar_ticks, float(self.confidence*100))
        cb.set_ticks(colorbar_ticks)


        plt.title(title, fontsize="large", fontweight="bold")


        # this is reasonable number of ticks so that tick labels won't overlap
        max_num_xticks = 7
        max_num_yticks = 20

        xticks_period = int(np_ceil(len(self.proportions)/max_num_xticks))
        yticks_period = int(np_ceil(len(self.proportions)/max_num_yticks))

        xperiodic_probs = [float(v) for v in self.proportions[::xticks_period]]
        yperiodic_probs = [float(v) for v in self.proportions[::yticks_period]]

        ax.xaxis.set_major_locator(ticker.MultipleLocator(xticks_period))
        ax.yaxis.set_major_locator(ticker.MultipleLocator(yticks_period))
        ax.tick_params(axis='x', labelsize=8)
        ax.tick_params(axis='y', labelsize=9)
        ax.tick_params(top=False)
        ax.tick_params(right=False)
        # ax.xaxis.set_tick_params(labeltop=False)
        # ax.yaxis.set_tick_params(labelright=False)

        # auto-calculated ticks are fine except for redundant first and last ticks
        xticks = ax.get_xticks().tolist()[1:-1]
        yticks = ax.get_yticks().tolist()[1:-1]
        ax.set_xticks(xticks)
        ax.set_yticks(yticks)
        ax.set_xticklabels(xperiodic_probs)
        ax.set_yticklabels(yperiodic_probs)


        self.figure = fig
        return self.figure


    def calculate_coverage_and_show_plot(self,
            sample_size1: int,
            sample_size2: int,
            proportions: proportions_type,
            confidence: float,

            plt_figure_title: str = "",
            title: str = "Coverage of {method_name}\nsamples: n1 = {sample_size1}, n2 = {sample_size2}",
            theme: plot_styles = "default",
            colors: Tuple[str,str,str,str,str] = ("gray", "purple", "white", "#b8df96", "green")
            ):
        self.calculate_coverage_analytically(sample_size1, sample_size2, proportions, confidence)
        self.plot_coverage(plt_figure_title, title, theme, colors)
        self.show_plot()

