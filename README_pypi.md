# CI methods analyser
A toolkit for measuring the efficacy of various methods for calculating a confidence interval.
Currently provides a toolkit for measuring the efficacy of methods for a confidence interval for the following statistics:

 - proportion
 - the difference between two proportions

This library was mainly inspired by the library:
["Five Confidence Intervals for Proportions That You Should Know About" by Dr. Dennis Robert](https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f)

## Dependencies
 - python >=3.8
 - python libs:
    - numpy
    - scipy
    - matplotlib
    - tqdm

## Applications

**Applied statistics and data science:** compare multiple CI methods to select the most appropriate for specific scenarios (by its accuracy at a specific range of true population properties, by computational performance, etc.)

**Education on statistics and CI:** demonstrates how different CI methods perform under various conditions, helps to understand the concept of CI by comparing methods for evaluation of accuracy of CI methods


## Usage

### **Testing Wald Interval - a popular method for calculating a confidence interval for proportion**

Wald Interval is defined as so:

<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/png.latex?%5Cbg_white%20%28w%5E-%2C%20w%5E&plus;%29%20%3D%20%5Chat%7Bp%7D%5C%2C%5Cpm%5C%2Cz%5Csqrt%7B%5Cfrac%7B%5Chat%7Bp%7D%281-%5Chat%7Bp%7D%29%7D%7Bn%7D%7D" alt="$$ (w^-, w^+) = p\,\pm\,z\sqrt{\frac{p(1-p)}{n}} $$" />
</div>

How well does it approximate the confidence interval?

Let's assess what would be the quality of produced 95%CI with this method by testing on a range of proportions. We'll take 100 true proportions, with 1% step `[0.001, 0.011, 0.021, ..., 0.991]`.


```python
from CI_methods_analyser import CImethodForProportion_efficacyToolkit as toolkit, methods_for_CI_for_proportion

toolkit(
    method=methods_for_CI_for_proportion.wald_interval, method_name="Wald Interval"
).calculate_coverage_and_show_plot(
    sample_size=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title="Wald Interval coverage"
)


input('press Enter to exit')
```


This outputs the image:

![Wald Interval - real coverage](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/wald_interval_p_0.001_0.999_0.01_n100_conf95.png)

The plot indicates the overall bad performance of the method and particularly poor performance for extreme proportions. While for some true proportions the calculated CI has true confidence of around 95%, most of the time the confidence is significantly lower. For the true proportions of <0.05 and >0.95 the true confidence of the generated CI is generally lower than 90%, as indicated by the steep descent on the left-most and right-most parts of the plot.

<hr>

*You really might want to use a different method. Check out this wonderful medium.com article by **Dr. Dennis Robert**:*
 - ***[Five Confidence Intervals for Proportions That You Should Know About](https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f)** [code in R]*

<hr>

<br>

The function `calculate_coverage_and_show_plot` that we just used is a shortcut. The code below does the same calculations and yields the same result. It relies on the public properties and methods, giving more control over parts of the calculation:

```python
from CI_methods_analyser import CImethodForProportion_efficacyToolkit as toolkit, methods_for_CI_for_proportion

# take an already implemented method for calculating CI for proportions
wald_interval = methods_for_CI_for_proportion.wald_interval

# initialize the toolkit
wald_interval_test_toolkit = toolkit(
    method=wald_interval, method_name="Wald Interval")


# calculate the real coverage that the method produces
# for each case of a true population proportion (taken from the list `proportions`)
wald_interval_test_toolkit.calculate_coverage_analytically(
    sample_size=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95)
# now you can access the calculated coverage and a few statistics:
# wald_interval_test_toolkit.coverage  # 1-d array of 0-100, the same shape as passed `proportions`
# NOTE: `proportions`, when passed as a tuple of 3 float strings, expands to a list of evenly spaced float values where the #0 value is begin, #1 is end, #2 is step.
# wald_interval_test_toolkit.average_coverage  # np.longdouble 0-100, avg of `coverage`
# wald_interval_test_toolkit.average_deviation  # np.longdouble 0-100, avg abs diff w/ `confidence`

# plots the calculated coverage in a matplotlib.pyplot figure
wald_interval_test_toolkit.plot_coverage(
    plt_figure_title="Wald Interval coverage")
# you can access the figure here:
# wald_interval_test_toolkit.figure

# shows the figure (non-blocking)
wald_interval_test_toolkit.show_plot()

# because show_plot() is non-blocking,
# you have to pause the execution in order for the figure to be rendered completely
input('press Enter to exit')
```

I expose some style/color settings used by matplotlib.

My preference goes to the **night light-friendly** styling:

```python
from CI_methods_analyser import CImethodForProportion_efficacyToolkit as toolkit, methods_for_CI_for_proportion


toolkit(
    method=methods_for_CI_for_proportion.wald_interval, method_name="Wald Interval"
).calculate_coverage_and_show_plot(
    sample_size=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title="Wald Interval coverage",
    theme='dark_background', plot_color="green", line_color="orange"
)


input('press Enter to exit')
```

![Wald Interval - real coverage (dark theme)](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/wald_interval_p_0.001_0.999_0.01_n100_conf95_dark.png)




<br>

### **Testing custom method for CI for proportion**

You can implement your own methods and test them:

```python
from CI_methods_analyser import CImethodForProportion_efficacyToolkit as toolkit
from CI_methods_analyser.math_functions import normal_z_score_two_tailed
from functools import lru_cache

# not a particularly good method for calculating CI for proportion
@lru_cache(100_000)
def im_telling_ya_test(x: int, n: int, conflevel: float = 0.95):
    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    return (
        p - 0.02*z,
        p + 0.02*z
    )


toolkit(
    method=im_telling_ya_test, method_name='"I\'m telling ya" test'
).calculate_coverage_and_show_plot(
    sample_size=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title='"I\'m telling ya" coverage',
    theme='dark_background', plot_color="green", line_color="orange"
)


input('press Enter to exit')

```
!["I'm telling ya" test - real coverage](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/im_telling_ya_test_p_0.001_0.999_0.01_n100_conf95_dark.png)


This is the kind of test one would not trust. It shows very unreliable performance for the majority of the true proportions, as indicated by an extremely high discrepancy between the "ordered" confidence level of 95% and the true confidence of the CI range provided by this method. This means the output CIs are generally smaller than should be, therefore there's less confidence that the true value lies within the range of a CI. One could say, this method overestimates its ability to generate a confident range.

<b>Let's try another custom method: "God is my witness" score</b>

```python
from CI_methods_analyser import CImethodForProportion_efficacyToolkit as toolkit
from CI_methods_analyser.math_functions import normal_z_score_two_tailed
from functools import lru_cache

# you could say, this method is "too good"
@lru_cache(100_000)
def God_is_my_witness_score(x: int, n: int, conflevel: float = 0.95):
    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    return (
        (0 + p)/2 - 0.005*z,
        (1 + p)/2 + 0.005*z
    )


toolkit(
    method=God_is_my_witness_score, method_name='"God is my witness" score'
).calculate_coverage_and_show_plot(
    sample_size=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title='"God is my witness" score coverage', theme='dark_background'
)

input('press Enter to exit')
```

!["God is my witness" score - real coverage](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/God_is_my_witness_score_p_0.001_0.999_0.01_n100_conf95_dark.png)


This method clearly overdid the estimates. While one expects 95%CI, the output range is less clear, as it allows for a very wide range of possibilities. In a stats lingo one would say that this method is way too conservative.


### **Testing methods for CI for the difference between two proportions**

Let's use the implemented **Pooled Z test**:

<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/gif.latex?%5Cbg_white%20%28%5Cdelta%5E-%2C%20%5Cdelta%5E&plus;%29%20%3D%20%5Chat%7Bp%7D_T%20-%20%5Chat%7Bp%7D_C%20%5Cpm%20z_%7B%5Calpha%7D%5Csqrt%7B%5Cbar%7Bp%7D%281-%5Cbar%7Bp%7D%29%28%5Cfrac%7B1%7D%7Bn_T%7D&plus;%5Cfrac%7B1%7D%7Bn_C%7D%29%7D" alt="$$ (\delta^-, \delta^+) = \hat{p}_T - \hat{p}_C \pm z_{\alpha}\sqrt{\bar{p}(1-\bar{p})(\frac{1}{n_T}+\frac{1}{n_C})} $$" />
</div>
, where:
<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/gif.latex?%5Cbg_white%20%5Cbar%7Bp%7D%20%3D%20%5Cfrac%7Bn_T%5Chat%7Bp%7D_T%20&plus;%20n_C%5Chat%7Bp%7D_C%7D%7Bn_T%20&plus;%20n_C%7D" alt="$$ \bar{p} = \frac{n_T\hat{p}_T + n_C\hat{p}_C}{n_T + n_C} $$" />
</div>


```python
from CI_methods_analyser import CImethodForDiffBetwTwoProportions_efficacyToolkit as toolkit_d, methods_for_CI_for_diff_betw_two_proportions as methods


toolkit_d(
    method=methods.Z_test_pooled, method_name='Z test pooled'
).calculate_coverage_and_show_plot(
    sample_size1=100, sample_size2=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title='Z test pooled', theme='dark_background',
)

input('press Enter to exit')
```


![Z test (unpooled) - real coverage](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/z_test_pooled_p_0.001_0.999_0.01_n1_100_n2_100_conf95.png)

As you can see, this test is generally perfect for close proportions (along `y = x` line) <b>[WHITE]</b>, unless proportions have extreme values, where confidence of the outputted CIs is lower than expected <b>[PURPLE]</b>

Also, this test is extremely conservative for the high and extreme differences between two proportions, i.e. for proportions whose values are far apart <b>[GREEN]</b>

<br>


You may want to change the color palette (although I wouldn't):


```python
from CI_methods_analyser import CImethodForDiffBetwTwoProportions_efficacyToolkit as toolkit_d, methods_for_CI_for_diff_betw_two_proportions as methods


toolkit_d(
    method=methods.Z_test_pooled, method_name='Z test pooled'
).calculate_coverage_and_show_plot(
    sample_size1=100, sample_size2=100, proportions=('0.001', '0.999', '0.01'), confidence=0.95,
    plt_figure_title='Z test pooled', theme='dark_background',
    colors=("gray", "purple", "white", "orange", "#d62728")
)

input('press Enter to exit')
```

![Z test (unpooled) - real coverage](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/z_test_pooled_p_0.001_0.999_0.01_n1_100_n2_100_conf95_hotcolors.png)


<br>
<br>

## NOTES

### Methods for measuring the efficacy of CI methods
Two ways can be used to calculate the efficacy of CI methods for a given confidence and a true population proportion:
 - approximately, with random simulation (as implemented in R by Dr. Dennis Robert, see link above). Here: `calculate_coverage_randomly`.
 - precisely, with the analytical solution. Here: `calculate_coverage_analytically`

<b>By default, always prefer the analytical solution.</b>

Sampling the same binomial distribution n times, as it's typically done, (called "random experiments", or "simulations") is inefficient, because the binomial distribution is already fully determined by the given true population proportion.

By relying on the binomial distribution from scipy, the analytical solution provides 100% accuracy for any method (defined as a python function), any confidence level, any true population proportion(s), any sample and population size(s).

Mathematical proof of the analytical solution:

![Proof of the analytical solution](https://github.com/Kukuster/CI_methods_analyser/raw/master/docs/2021-05-08_ci-method-for-proportions_analytical-solution.jpg)


Both "simulation" and "analytical" methods are implemented for CI for both statistics: *proportion*, and *the difference between two proportions*. For the precise analytical solution, an optimization was made. Theoretically, it is lossy, but practically, the error is always negligible (as shown by `test_z_precision_difference.py`) and is less significant than a 64-bit floating point precision error between the closest `float` representation and the true `Real` value. Optimization is regulated with the parameter `z_precision`, which is automatically estimated by default.



<br>

## Various links
**1. Equivalence and Noninferiority Testing (as I understand, are fancy terms for 2-sided and 1-sided p tests for the difference between two proportions)**
 - **[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf)**
 - **[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Non-Inferiority_Tests_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Non-Inferiority_Tests_for_the_Difference_Between_Two_Proportions.pdf)**
 - [https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Two_Proportions-Non-Inferiority,_Superiority,_Equivalence,_and_Two-Sided_Tests_vs_a_Margin.pdf](https://www.ncss.com/wp-content/themes/ncss/pdf/Procedures/NCSS/Two_Proportions-Non-Inferiority,_Superiority,_Equivalence,_and_Two-Sided_Tests_vs_a_Margin.pdf) 
 - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3019319/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3019319/)
 - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2701110/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2701110/)
 - [https://pubmed.ncbi.nlm.nih.gov/9595617/](https://pubmed.ncbi.nlm.nih.gov/9595617/)
 - [http://thescipub.com/pdf/10.3844/amjbsp.2010.23.31](http://thescipub.com/pdf/10.3844/amjbsp.2010.23.31) 

**2. Biostatistics course (Dr. Nicolas Padilla Raygoza, et al.)**
 - [https://docs.google.com/presentation/d/1t1DowyVDDRFYGHDlJgmYMRN4JCrvFl3q/edit#slide=id.p1](https://docs.google.com/presentation/d/1t1DowyVDDRFYGHDlJgmYMRN4JCrvFl3q/edit#slide=id.p1) 
 - [https://www.google.com/search?q=Dr.+Sc.+Nicolas+Padilla+Raygoza+Biostatistics+course+Part+10&oq=Dr.+Sc.+Nicolas+Padilla+Raygoza+Biostatistics+course+Part+10&aqs=chrome..69i57.3448j0j7&sourceid=chrome&ie=UTF-8](https://www.google.com/search?q=Dr.+Sc.+Nicolas+Padilla+Raygoza+Biostatistics+course+Part+10&oq=Dr.+Sc.+Nicolas+Padilla+Raygoza+Biostatistics+course+Part+10&aqs=chrome..69i57.3448j0j7&sourceid=chrome&ie=UTF-8) 
 - [https://slideplayer.com/slide/9837395/](https://slideplayer.com/slide/9837395/)

**3. Using z-test instead of a binomial test:**
 - When can use [https://stats.stackexchange.com/questions/424446/when-can-we-use-a-z-test-instead-of-a-binomial-test](https://stats.stackexchange.com/questions/424446/when-can-we-use-a-z-test-instead-of-a-binomial-test) 
 - How to use [https://cogsci.ucsd.edu/~dgroppe/STATZ/binomial_ztest.pdf](https://cogsci.ucsd.edu/~dgroppe/STATZ/binomial_ztest.pdf) 

