# imports
# for 100% precision fractional operations (doesn't support most math functions like sqrt)
from decimal import Decimal
from typing import Callable, Generator, Iterable, List, Tuple, Union, Literal
# for high precision float operations (supports most math functions like sqrt, often faster than decimal)
from bigfloat import BigFloat
from matplotlib import pyplot as plt
from scipy.stats import norm, binom
import numpy as np
import math
# import csv
import pandas as pd
import time
from functools import lru_cache



### FORMATTING FUNCTIONS ###

def floatToStr(inputValue: Union[float, BigFloat, Decimal], precision: int = 10):
    return (f'%.{precision}f' % inputValue).rstrip('0').rstrip('.')


### DATA FUNCTIONS ###

def BigFloat_to_Decimal(x):
    try:
        return (Decimal(e.__str__()) for e in x)
    except TypeError:
        return Decimal(x.__str__())


def Decimal_to_BigFloat(x):
    try:
        return (BigFloat(e.__str__()) for e in x)
    except TypeError:
        return BigFloat(x.__str__())


# like python range, but for floats
def frange(x: Union[float, Decimal], y: Union[float, Decimal], jump: Union[float, Decimal]) -> Generator[float, None, None]:
    while x <= y:
        yield float(x)
        x = Decimal(x) + Decimal(jump)



### MATH FUNCTIONS ###

@lru_cache(1)
def zScore_normal(conflevel: float = 0.95):
    z: float = norm.ppf((1+conflevel)/2)
    return abs(z)


@lru_cache(50000)
def significant_range(n: int, p: float, sds: float):
    """
    Calculates range of x values that span *sds* standard deviations from the mean of a binomial distribution with parameters *n* and *p*
    """
    M = n*p
    sd = math.sqrt(n*p*(1-p))
    (x_from, x_to) = max(0, np.floor(M - sds*sd) - 1), min(n, np.ceil(M + sds*sd) + 1)
    return int(x_from), int(x_to)



### CI METHODS FOR PROPORTIONS ###

CI_method = Callable[
    [int, int, Union[float, None], Union[float, None]],
    Tuple[float, float]
]


@lru_cache(50000)
def wald_interval(x: int, n: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None):
    # LaTeX: $$(w^-, w^+) = \hat{p}\,\pm\,z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
    """Calculates confidence interval for proportions using Wald Interval method

    `x` - succeeded trials

    `n` - total trials

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    if x > n:
        raise ValueError(f"Number of succeeded trials (x) has to be no more than number of total trials (n). x = {x} and n = {n} were passed")
    if z is None:
        if conflevel is None:
            conflevel = 0.95
        z = zScore_normal(conflevel)

    p = float(x)/n
    sd = math.sqrt((p*(1-p))/n)
    z_sd = z*sd
    ci = (
        p - z_sd,
        p + z_sd
    )
    return ci


@lru_cache(50000)
def wilson_score_interval(x: int, n: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None):
    # LaTeX: $$(w^-, w^+) = \frac{p + z^2/2n \pm z\sqrt{p(1-p)/n + z^2/4n^2}}{1+z^2/n}$$
    """Calculates confidence interval for proportions using Wilson Score Interval method

    `x` - succeeded trials

    `n` - total trials

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    if x > n:
        raise ValueError(f"Number of succeeded trials (x) has to be no more than number of total trials (n). x = {x} and n = {n} were passed")
    if z is None:
        if conflevel is None:
            conflevel = 0.95
        z = zScore_normal(conflevel)
    
    p = float(x)/n
    denom = 1 + ((z**2) / n)
    mean = p + ((z**2)/(2*n))
    diff = z * math.sqrt(p*(1-p)/n + (z**2)/(4*n**2))
    ci = (
        (mean-diff)/denom,
        (mean+diff)/denom
    )
    return ci


@lru_cache(50000)
def wilson_score_interval_continuity_corrected(x: int, n: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None):
    # LaTeX:
    # $$w_{cc}^- = \frac{2np + z^2 - (z\sqrt{z^2 - 1/n + 4np(1-p) + (4p-2)} + 1)}{2(n+z^2)}$$
    # $$w_{cc}^+ = \frac{2np + z^2 + (z\sqrt{z^2 - 1/n + 4np(1-p) - (4p-2)} + 1)}{2(n+z^2)}$$
    # or, simplified:
    # $$e = 2np + z^2;\,\,\, f = z^2 - 1/n + 4np(1-p);\,\,\, g = (4p - 2);\,\,\, h = 2(n+z^2)$$
    # $$w_{cc}^- = \frac{e - (z\sqrt{f+g} + 1)}{h}$$
    # $$w_{cc}^+ = \frac{e + (z\sqrt{f-g} + 1)}{h}$$
    """Calculates confidence interval for proportions using Wilson Score Interval method with correction for continuity

    `x` - succeeded trials

    `n` - total trials

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    if x > n:
        raise ValueError(f"Number of succeeded trials (x) has to be no more than number of total trials (n). x = {x} and n = {n} were passed")
    if z is None:
        if conflevel is None:
            conflevel = 0.95
        z = zScore_normal(conflevel)
    
    p = float(x)/n
    e = 2*n*p + z**2
    f = z**2 - 1/n + 4*n*p*(1-p)
    g = (4*p - 2)
    h = 2*(n+z**2)
    ci = (
        (e - (z*math.sqrt(f+g) + 1))/h,
        (e + (z*math.sqrt(f-g) + 1))/h
    )
    return ci


@lru_cache(50000)
def wilson_score_interval_continuity_semicorrected(x: int, n: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None):
    """Calculates confidence interval for proportions using two Wilson Score Interval methods
    (arithmetic mean of ordinary and continuity-corrected methods)

    `x` - succeeded trials

    `n` - total trials

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    if x > n:
        raise ValueError(
            f"Number of succeeded trials (x) has to be no more than number of total trials (n). x = {x} and n = {n} were passed")
    if z is None:
        if conflevel is None:
            conflevel = 0.95
        z = zScore_normal(conflevel)
    
    uncorrected = wilson_score_interval(x, n, conflevel, z)
    corrected   = wilson_score_interval_continuity_corrected(x, n, conflevel, z)
    ci = (
        (corrected[0]+uncorrected[0])/2,
        (corrected[1]+uncorrected[1])/2
    )
    return ci



### MAIN FUNCTIONS ###

def calculate_coverage(numSamples: int, numTrials: int, probs: Iterable[float], conflevel: float, method: CI_method, randomly: bool = True) -> List[float]:
    if not 0 < conflevel < 1:
        raise ValueError(
            f"confidence level has to be real value between 0 and 1. Got: conflevel={conflevel}")

    coverage = []
    z = zScore_normal(conflevel)

    if randomly:
        for prob in list(probs):
            x = np.random.binomial(numTrials, prob, numSamples)
            cis = [method(x[j], numTrials, None, z) for j in range(0, numSamples)]
            covered = [int(ci[0] < prob < ci[1]) for ci in cis]
            thiscoverage = (sum(covered)/numSamples) * 100
            coverage.append(thiscoverage)
            print(f"prob ={prob:9}; coverage ={thiscoverage:6.2f}")
    else:
        for prob in list(probs):
            x_from, x_to = significant_range(n=numTrials, p=prob, sds=4.7)
            xs = range(x_from, x_to+1)
            len_xs = len(xs)
            print(f"range(x_from, x_to) = {xs}")
            cis = [method(x, numTrials, None, z) for x in xs]
            covered = [int(ci[0] < prob < ci[1]) for ci in cis]
            thiscoverage = sum([covered[i]*binom.pmf(xs[i],numTrials,prob) for i in range(len(xs))]) * 100
            coverage.append(thiscoverage)
            print(f"prob ={prob:9}; coverage ={thiscoverage:6.2f}")

    return coverage


def plot_coverage(probs: Iterable[float], coverage: List[float], conflevel: float, title: str, xlabel: str, ylabel: str):
    plt.plot(list(probs), coverage, color='green', marker=',', linestyle='solid', zorder=5)
    plt.axhline(conflevel*100, color='orange', linestyle=":", zorder=0)
    x1, x2, y1, y2 = plt.axis()
    plt.axis((x1, x2, 50, 100))
    plt.title(title, fontsize="large", fontweight="bold")
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    x1, x2, y1, y2 = plt.axis()

    avg_deviation = Decimal(0)
    conflevel_percent = Decimal(conflevel*100)
    for cov in coverage:
        deviation = abs(Decimal(cov)-conflevel_percent)
        # print(f"deviation = {floatToStr(deviation, 2)}")
        avg_deviation += deviation
    avg_deviation = avg_deviation/len(coverage)
    plt.text((x1+x2)/2, (y1+5),
        f"average deviation from {floatToStr(conflevel*100, 2)}% point = {floatToStr(avg_deviation, 4)} (coverage %)",
        ha="center", fontstyle="italic", zorder=10)
    plt.xticks(fontsize=8)
    plt.ticklabel_format(scilimits=(-3,3), useMathText=True)


def calculate_and_plot_coverage(numSamples: int, numTrials: int,
                                probs: Iterable[float], conflevel: float,
                                method: CI_method, methodname: str):
    start_time = time.time()
    coverage = calculate_coverage(numSamples, numTrials, probs, conflevel, method)
    print("--- %s seconds ---" % (time.time() - start_time))
    plot_coverage(probs, coverage, conflevel, title=f"Coverage of {methodname}\n{numSamples} samples ✕ {numTrials} trials",
              xlabel="True Proportion (Population Proportion)", ylabel=f"Coverage (%) for {floatToStr(conflevel*100, 2)}%CI")





### EXE ###

numSamples = 10000
# numTrials = 40000
step = Decimal('0.003')
probs = list(frange(Decimal('0.001'), Decimal('0.999'), step))
# step = Decimal('0.000001')
# probs = list(frange(Decimal('0.000001'), Decimal('0.000199'), step))
conflevel = 0.95

i = 0
for (numTrials) in [
    (100),
    # (1000),
    # (20000),
    # (21720),
    # (37706),
    # (40000),
]:
    for (method, methodname, method_filename) in [
        (wald_interval, "Wald Interval", 'wald'),
        # (wilson_score_interval, "Wilson Score Interval", "wsi"),
        # (wilson_score_interval_continuity_corrected,
        # "Wilson Score Interval (continuity-corrected)", "wsicc"),
        # (wilson_score_interval_continuity_semicorrected,
        # "Wilson Score Interval (continuity-semi-corrected)", "wsisc"),
    ]:
        print(
            f"name = {methodname}, numTrials = {numTrials}, numSamples = {numSamples}, probs = {probs[0]}-{probs[-1]}..{step}, conflevel = {conflevel}")


        # calculate_and_plot_coverage(numSamples, numTrials, probs, conflevel, method, methodname)

        start_time = time.time()
        coverage = calculate_coverage(numSamples, numTrials, probs, conflevel, method, False)
        print("--- %s seconds ---" % (time.time() - start_time))

        for (theme, theme_filename) in [
            # ("default", ""),
            ("dark_background", "_dark")
        ]:
            plt.style.use(theme)
            i += 1
            plt.figure(i)
            plot_coverage(probs, coverage, conflevel, title=f"Coverage of {methodname}\n{numSamples} samples ✕ {numTrials} trials",
                    xlabel="True Proportion (Population Proportion)", ylabel=f"Coverage (%) for {floatToStr(conflevel*100, 2)}%CI")

            # plt.savefig(
            #     f"{method_filename}_pfrom{probs[0]}_pto{probs[-1]}_pstep{step}_trials{numTrials}_samples{numSamples}{theme_filename}.png")


plt.show()



