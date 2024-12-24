<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px; margin-bottom: 1px;" src="https://img.shields.io/badge/dynamic/json?url=https://packages.ecosyste.ms/api/v1/registries/pypi.org/packages/ci-methods-analyser&label=downloads&query=$.downloads" alt="number of downloads" />
    <img style="display: inline-block; margin: 5px; margin-bottom: 1px;" src="https://img.shields.io/badge/dynamic/json?url=https://packages.ecosyste.ms/api/v1/registries/pypi.org/packages/ci-methods-analyser&label=within&query=$.downloads_period" alt="downloads period" />
</div>

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

## Installation

https://pypi.org/project/CI-methods-analyser/


## Applications

**Applied statistics and data science:** compare multiple CI methods to select the most appropriate for specific scenarios (by its accuracy at a specific range of true population properties, by computational performance, etc.)

**Education on statistics and CI:** demonstrates how different CI methods perform under various conditions, helps to understand the concept of CI by comparing methods for evaluation of accuracy of CI methods


## Usage

### <u>Testing Wald Interval - a popular method for calculating a confidence interval for proportion</u>

Wald Interval is defined as so:

<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/png.latex?%5Cbg_black%20%28w%5E-%2C%20w%5E&plus;%29%20%3D%20%5Chat%7Bp%7D%5C%2C%5Cpm%5C%2Cz%5Csqrt%7B%5Cfrac%7B%5Chat%7Bp%7D%281-%5Chat%7Bp%7D%29%7D%7Bn%7D%7D" alt="$$ (w^-, w^+) = p\,\pm\,z\sqrt{\frac{p(1-p)}{n}} $$" />
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

### <u>Testing custom method for CI for proportion</u>

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


### <u>Testing methods for CI for the difference between two proportions</u>

Let's use the implemented **Pooled Z test**:

<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/gif.latex?%5Cbg_black%20%28%5Cdelta%5E-%2C%20%5Cdelta%5E&plus;%29%20%3D%20%5Chat%7Bp%7D_T%20-%20%5Chat%7Bp%7D_C%20%5Cpm%20z_%7B%5Calpha%7D%5Csqrt%7B%5Cbar%7Bp%7D%281-%5Cbar%7Bp%7D%29%28%5Cfrac%7B1%7D%7Bn_T%7D&plus;%5Cfrac%7B1%7D%7Bn_C%7D%29%7D" alt="$$ (\delta^-, \delta^+) = \hat{p}_T - \hat{p}_C \pm z_{\alpha}\sqrt{\bar{p}(1-\bar{p})(\frac{1}{n_T}+\frac{1}{n_C})} $$" />
</div>
, where:
<div style="text-align: center; margin: auto">
    <img style="display: inline-block; margin: 5px" src="https://latex.codecogs.com/gif.latex?%5Cbg_black%20%5Cbar%7Bp%7D%20%3D%20%5Cfrac%7Bn_T%5Chat%7Bp%7D_T%20&plus;%20n_C%5Chat%7Bp%7D_C%7D%7Bn_T%20&plus;%20n_C%7D" alt="$$ \bar{p} = \frac{n_T\hat{p}_T + n_C\hat{p}_C}{n_T + n_C} $$" />
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



## I accept donations!

### Paypal

<p>
<!--   <a href="https://www.paypal.com/donate/?hosted_button_id=485PXFAM75G4E">
      <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif" alt="paypal">
  </a> -->
  <a href="https://www.paypal.com/donate/?hosted_button_id=485PXFAM75G4E">
      <img src="https://www.paypalobjects.com/en_US/i/btn/btn_donate_SM.gif" alt="paypal">
  </a>
</p>

### Cryptocurrency

You can add a transaction message with the name of a project or a custom message if your wallet and the blockchain support this

Preferred blockchains:

blockchain | address |  
--- | --- | ---
<a href="javascript:void(0)" style="cursor: default;" alt="Donate via Bitcoin"><img src="https://img.shields.io/badge/-Bitcoin-402607?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjRjc5MzFBIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+Qml0Y29pbjwvdGl0bGU+PHBhdGggZD0iTTIzLjYzOCAxNC45MDRjLTEuNjAyIDYuNDMtOC4xMTMgMTAuMzQtMTQuNTQyIDguNzM2QzIuNjcgMjIuMDUtMS4yNDQgMTUuNTI1LjM2MiA5LjEwNSAxLjk2MiAyLjY3IDguNDc1LTEuMjQzIDE0LjkuMzU4YzYuNDMgMS42MDUgMTAuMzQyIDguMTE1IDguNzM4IDE0LjU0OHYtLjAwMnptLTYuMzUtNC42MTNjLjI0LTEuNTktLjk3NC0yLjQ1LTIuNjQtMy4wM2wuNTQtMi4xNTMtMS4zMTUtLjMzLS41MjUgMi4xMDdjLS4zNDUtLjA4Ny0uNzA1LS4xNjctMS4wNjQtLjI1bC41MjYtMi4xMjctMS4zMi0uMzMtLjU0IDIuMTY1Yy0uMjg1LS4wNjctLjU2NS0uMTMyLS44NC0uMmwtMS44MTUtLjQ1LS4zNSAxLjQwN3MuOTc1LjIyNS45NTUuMjM2Yy41MzUuMTM2LjYzLjQ4Ni42MTUuNzY2bC0xLjQ3NyA1LjkyYy0uMDc1LjE2Ni0uMjQuNDA2LS42MTQuMzE0LjAxNS4wMi0uOTYtLjI0LS45Ni0uMjRsLS42NiAxLjUxIDEuNzEuNDI2LjkzLjI0Mi0uNTQgMi4xOSAxLjMyLjMyNy41NC0yLjE3Yy4zNi4xLjcwNS4xOSAxLjA1LjI3M2wtLjUxIDIuMTU0IDEuMzIuMzMuNTQ1LTIuMTljMi4yNC40MjcgMy45My4yNTcgNC42NC0xLjc3NC41Ny0xLjYzNy0uMDMtMi41OC0xLjIxNy0zLjE5Ni44NTQtLjE5MyAxLjUtLjc2IDEuNjgtMS45M2guMDF6bS0zLjAxIDQuMjJjLS40MDQgMS42NC0zLjE1Ny43NS00LjA1LjUzbC43Mi0yLjljLjg5Ni4yMyAzLjc1Ny42NyAzLjMzIDIuMzd6bS40MS00LjI0Yy0uMzcgMS40OS0yLjY2Mi43MzUtMy40MDUuNTVsLjY1NC0yLjY0Yy43NDQuMTggMy4xMzcuNTI0IDIuNzUgMi4wODR2LjAwNnoiLz48L3N2Zz4=" /></a> |  `bc1pjd2c4xcgq978979htc9admycue4nqqhda3vwsc38agked8yya50qz454xc` | 
<a href="javascript:void(0)" style="cursor: default;" alt="Donate via Ethereum"><img src="https://img.shields.io/badge/-Ethereum-6784c7?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjM0MzQzNEIiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+RXRoZXJldW08L3RpdGxlPjxwYXRoIGQ9Ik0xMS45NDQgMTcuOTdMNC41OCAxMy42MiAxMS45NDMgMjRsNy4zNy0xMC4zOC03LjM3MiA0LjM1aC4wMDN6TTEyLjA1NiAwTDQuNjkgMTIuMjIzbDcuMzY1IDQuMzU0IDcuMzY1LTQuMzVMMTIuMDU2IDB6Ii8+PC9zdmc+" /></a> |  `0x176D1b6c3Fc1db5f7f967Fdc735f8267cCe741F3` | <span>![Tether](https://raw.githubusercontent.com/Kukuster/Kukuster/refs/heads/master/tether_20x20.svg)</span> supports USDT ERC-20
<a href="javascript:void(0)" style="cursor: default;" alt="Donate via TRON"><img src="https://img.shields.io/badge/-TRON-5C0E0E?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjRkYwNjBBIiBpZD0iQ2FscXVlXzEiIGRhdGEtbmFtZT0iQ2FscXVlIDEiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgdmlld0JveD0iMCAwIDY0IDY0Ij48ZGVmcz48c3R5bGU+LmNscy0xe2ZpbGw6I2ZmMDYwYTt9PC9zdHlsZT48L2RlZnM+PHRpdGxlPnRyb248L3RpdGxlPjxnIGlkPSJ0cm9uIj48cGF0aCBjbGFzcz0iY2xzLTEiIGQ9Ik02MS41NSwxOS4yOGMtMy0yLjc3LTcuMTUtNy0xMC41My0xMGwtLjItLjE0YTMuODIsMy44MiwwLDAsMC0xLjExLS42MmwwLDBDNDEuNTYsNywzLjYzLS4wOSwyLjg5LDBhMS40LDEuNCwwLDAsMC0uNTguMjJMMi4xMi4zN2EyLjIzLDIuMjMsMCwwLDAtLjUyLjg0bC0uMDUuMTN2LjcxbDAsLjExQzUuODIsMTQuMDUsMjIuNjgsNTMsMjYsNjIuMTRjLjIuNjIuNTgsMS44LDEuMjksMS44NmguMTZjLjM4LDAsMi0yLjE0LDItMi4xNFM1OC40MSwyNi43NCw2MS4zNCwyM2E5LjQ2LDkuNDYsMCwwLDAsMS0xLjQ4QTIuNDEsMi40MSwwLDAsMCw2MS41NSwxOS4yOFpNMzYuODgsMjMuMzcsNDkuMjQsMTMuMTJsNy4yNSw2LjY4Wm0tNC44LS42N0wxMC44LDUuMjZsMzQuNDMsNi4zNVpNMzQsMjcuMjdsMjEuNzgtMy41MS0yNC45LDMwWk03LjkxLDcsMzAuMywyNiwyNy4wNiw1My43OFoiLz48L2c+PC9zdmc+" /></a> | `TMuNqEgEeBQ2GseWsqgaSdbtqasnJi8ePw` | <span>![Tether](https://raw.githubusercontent.com/Kukuster/Kukuster/refs/heads/master/tether_20x20.svg)</span> supports USDT TRC-20



<details>
  <summary>Alternative options (Ethereum L2, LN, EVM)</summary>
  
  blockchain | address
  --- | ---
  <a href="javascript:void(0)" style="cursor: default;" alt="Donate via Polygon"><img src="https://img.shields.io/badge/-Polygon-2a0c60?logo=data:image/svg%2bxml;base64,PHN2ZyBmaWxsPSIjN0IzRkU0IiByb2xlPSJpbWciIHZpZXdCb3g9IjAgMCAyNCAyNCIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj48dGl0bGU+UG9seWdvbjwvdGl0bGU+PHBhdGggZD0ibTE3LjgyIDE2LjM0MiA1LjY5Mi0zLjI4N0EuOTguOTggMCAwIDAgMjQgMTIuMjFWNS42MzVhLjk4Ljk4IDAgMCAwLS40ODgtLjg0NmwtNS42OTMtMy4yODZhLjk4Ljk4IDAgMCAwLS45NzcgMEwxMS4xNSA0Ljc4OWEuOTguOTggMCAwIDAtLjQ4OS44NDZ2MTEuNzQ3TDYuNjcgMTkuNjg2bC0zLjk5Mi0yLjMwNHYtNC42MWwzLjk5Mi0yLjMwNCAyLjYzMyAxLjUyVjguODk2TDcuMTU4IDcuNjU4YS45OC45OCAwIDAgMC0uOTc3IDBMLjQ4OCAxMC45NDVhLjk4Ljk4IDAgMCAwLS40ODguODQ2djYuNTczYS45OC45OCAwIDAgMCAuNDg4Ljg0N2w1LjY5MyAzLjI4NmEuOTgxLjk4MSAwIDAgMCAuOTc3IDBsNS42OTItMy4yODZhLjk4Ljk4IDAgMCAwIC40ODktLjg0NlY2LjYxOGwuMDcyLS4wNDEgMy45Mi0yLjI2MyAzLjk5IDIuMzA1djQuNjA5bC0zLjk5IDIuMzA0LTIuNjMtMS41MTd2My4wOTJsMi4xNCAxLjIzNmEuOTgxLjk4MSAwIDAgMCAuOTc4IDB2LS4wMDFaIi8+PC9zdmc+" /></a> |  `0x176D1b6c3Fc1db5f7f967Fdc735f8267cCe741F3`
  <a href="javascript:void(0)" style="cursor: default;" alt="Donate via Base"><img src="https://img.shields.io/badge/-Base-152846?logo=data:image/svg%2bxml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA2NCA2NCIgeG1sOnNwYWNlPSJwcmVzZXJ2ZSIgd2lkdGg9IjMwcHgiIGhlaWdodD0iMzBweCI+PHBhdGggZmlsbD0iI0ZGRkZGRiIgZD0iTTYzLjYgMzJjMCAxNy40LTE0LjIgMzEuNi0zMS42IDMxLjZDMTUuNSA2My42IDEuOSA1MC45LjUgMzQuN2g0MS43di01LjNILjVDMS45IDEzLjEgMTUuNS40IDMyIC40IDQ5LjUuNCA2My42IDE0LjYgNjMuNiAzMnoiPjwvcGF0aD48L3N2Zz4=" /></a> |  `0x176D1b6c3Fc1db5f7f967Fdc735f8267cCe741F3`
  <a href="javascript:void(0)" style="cursor: default;" alt="Donate via Arbitrum"><img src="https://img.shields.io/badge/-Arbitrum-3F3F3F?logo=data:image/svg%2bxml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB4bWxuczp4b2RtPSJodHRwOi8vd3d3LmNvcmVsLmNvbS9jb3JlbGRyYXcvb2RtLzIwMDMiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyIgeG1sbnM6eGxpbms9Imh0dHA6Ly93d3cudzMub3JnLzE5OTkveGxpbmsiIHZlcnNpb249IjEuMSIgaWQ9IkxheWVyXzEiIHg9IjBweCIgeT0iMHB4IiB2aWV3Qm94PSIwIDAgMjUwMCAyNTAwIiBzdHlsZT0iZW5hYmxlLWJhY2tncm91bmQ6bmV3IDAgMCAyNTAwIDI1MDA7IiB4bWw6c3BhY2U9InByZXNlcnZlIj4KPHN0eWxlIHR5cGU9InRleHQvY3NzIj4KCS5zdDB7ZmlsbDpub25lO30KCS5zdDF7ZmlsbDojMjEzMTQ3O30KCS5zdDJ7ZmlsbDojMTJBQUZGO30KCS5zdDN7ZmlsbDojOURDQ0VEO30KCS5zdDR7ZmlsbDojRkZGRkZGO30KPC9zdHlsZT4KPGcgaWQ9IkxheWVyX3gwMDIwXzEiPgoJPGcgaWQ9Il8yNDA1NTg4NDc3MjMyIj4KCQk8cmVjdCBjbGFzcz0ic3QwIiB3aWR0aD0iMjUwMCIgaGVpZ2h0PSIyNTAwIj48L3JlY3Q+CgkJPGc+CgkJCTxnPgoJCQkJPHBhdGggY2xhc3M9InN0MSIgZD0iTTIyNiw3NjB2OTgwYzAsNjMsMzMsMTIwLDg4LDE1Mmw4NDksNDkwYzU0LDMxLDEyMSwzMSwxNzUsMGw4NDktNDkwYzU0LTMxLDg4LTg5LDg4LTE1MlY3NjAgICAgICBjMC02My0zMy0xMjAtODgtMTUybC04NDktNDkwYy01NC0zMS0xMjEtMzEtMTc1LDBMMzE0LDYwOGMtNTQsMzEtODcsODktODcsMTUySDIyNnoiPjwvcGF0aD4KCQkJCTxnPgoJCQkJCTxnPgoJCQkJCQk8Zz4KCQkJCQkJCTxwYXRoIGNsYXNzPSJzdDIiIGQ9Ik0xNDM1LDE0NDBsLTEyMSwzMzJjLTMsOS0zLDE5LDAsMjlsMjA4LDU3MWwyNDEtMTM5bC0yODktNzkzQzE0NjcsMTQyMiwxNDQyLDE0MjIsMTQzNSwxNDQweiI+PC9wYXRoPgoJCQkJCQk8L2c+CgkJCQkJCTxnPgoJCQkJCQkJPHBhdGggY2xhc3M9InN0MiIgZD0iTTE2NzgsODgyYy03LTE4LTMyLTE4LTM5LDBsLTEyMSwzMzJjLTMsOS0zLDE5LDAsMjlsMzQxLDkzNWwyNDEtMTM5TDE2NzgsODgzVjg4MnoiPjwvcGF0aD4KCQkJCQkJPC9nPgoJCQkJCTwvZz4KCQkJCTwvZz4KCQkJCTxnPgoJCQkJCTxwYXRoIGNsYXNzPSJzdDMiIGQ9Ik0xMjUwLDE1NWM2LDAsMTIsMiwxNyw1bDkxOCw1MzBjMTEsNiwxNywxOCwxNywzMHYxMDYwYzAsMTItNywyNC0xNywzMGwtOTE4LDUzMGMtNSwzLTExLDUtMTcsNSAgICAgICBzLTEyLTItMTctNWwtOTE4LTUzMGMtMTEtNi0xNy0xOC0xNy0zMFY3MTljMC0xMiw3LTI0LDE3LTMwbDkxOC01MzBjNS0zLDExLTUsMTctNWwwLDBWMTU1eiBNMTI1MCwwYy0zMywwLTY1LDgtOTUsMjVMMjM3LDU1NSAgICAgICBjLTU5LDM0LTk1LDk2LTk1LDE2NHYxMDYwYzAsNjgsMzYsMTMwLDk1LDE2NGw5MTgsNTMwYzI5LDE3LDYyLDI1LDk1LDI1czY1LTgsOTUtMjVsOTE4LTUzMGM1OS0zNCw5NS05Niw5NS0xNjRWNzE5ICAgICAgIGMwLTY4LTM2LTEzMC05NS0xNjRMMTM0NCwyNWMtMjktMTctNjItMjUtOTUtMjVsMCwwSDEyNTB6Ij48L3BhdGg+CgkJCQk8L2c+CgkJCQk8cG9seWdvbiBjbGFzcz0ic3QxIiBwb2ludHM9IjY0MiwyMTc5IDcyNywxOTQ3IDg5NywyMDg4IDczOCwyMjM0ICAgICAiPjwvcG9seWdvbj4KCQkJCTxnPgoJCQkJCTxwYXRoIGNsYXNzPSJzdDQiIGQ9Ik0xMTcyLDY0NEg5MzljLTE3LDAtMzMsMTEtMzksMjdMNDAxLDIwMzlsMjQxLDEzOWw1NTAtMTUwN2M1LTE0LTUtMjgtMTktMjhMMTE3Miw2NDR6Ij48L3BhdGg+CgkJCQkJPHBhdGggY2xhc3M9InN0NCIgZD0iTTE1ODAsNjQ0aC0yMzNjLTE3LDAtMzMsMTEtMzksMjdMNzM4LDIyMzNsMjQxLDEzOWw2MjAtMTcwMWM1LTE0LTUtMjgtMTktMjhWNjQ0eiI+PC9wYXRoPgoJCQkJPC9nPgoJCQk8L2c+CgkJPC9nPgoJPC9nPgo8L2c+Cjwvc3ZnPgo=" /></a> |  `0x176D1b6c3Fc1db5f7f967Fdc735f8267cCe741F3`
  <a href="javascript:void(0)" style="cursor: default;" alt="Donate via Avalanche"><img src="https://img.shields.io/badge/-Avalanche-4B2224?logo=data:image/svg%2bxml;base64,PHN2ZyB3aWR0aD0iMTUwMyIgaGVpZ2h0PSIxNTA0IiB2aWV3Qm94PSIwIDAgMTUwMyAxNTA0IiBmaWxsPSJub25lIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgo8cmVjdCB4PSIyODciIHk9IjI1OCIgd2lkdGg9IjkyOCIgaGVpZ2h0PSI4NDQiIGZpbGw9IndoaXRlIi8+CjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgY2xpcC1ydWxlPSJldmVub2RkIiBkPSJNMTUwMi41IDc1MkMxNTAyLjUgMTE2Ni43NyAxMTY2LjI3IDE1MDMgNzUxLjUgMTUwM0MzMzYuNzM0IDE1MDMgMC41IDExNjYuNzcgMC41IDc1MkMwLjUgMzM3LjIzNCAzMzYuNzM0IDEgNzUxLjUgMUMxMTY2LjI3IDEgMTUwMi41IDMzNy4yMzQgMTUwMi41IDc1MlpNNTM4LjY4OCAxMDUwLjg2SDM5Mi45NEMzNjIuMzE0IDEwNTAuODYgMzQ3LjE4NiAxMDUwLjg2IDMzNy45NjIgMTA0NC45NkMzMjcuOTk5IDEwMzguNSAzMjEuOTExIDEwMjcuOCAzMjEuMTczIDEwMTUuOTlDMzIwLjYxOSAxMDA1LjExIDMyOC4xODQgOTkxLjgyMiAzNDMuMzEyIDk2NS4yNTVMNzAzLjE4MiAzMzAuOTM1QzcxOC40OTUgMzAzLjk5OSA3MjYuMjQzIDI5MC41MzEgNzM2LjAyMSAyODUuNTVDNzQ2LjUzNyAyODAuMiA3NTkuMDgzIDI4MC4yIDc2OS41OTkgMjg1LjU1Qzc3OS4zNzcgMjkwLjUzMSA3ODcuMTI2IDMwMy45OTkgODAyLjQzOCAzMzAuOTM1TDg3Ni40MiA0NjAuMDc5TDg3Ni43OTcgNDYwLjczOEM4OTMuMzM2IDQ4OS42MzUgOTAxLjcyMyA1MDQuMjg5IDkwNS4zODUgNTE5LjY2OUM5MDkuNDQzIDUzNi40NTggOTA5LjQ0MyA1NTQuMTY5IDkwNS4zODUgNTcwLjk1OEM5MDEuNjk1IDU4Ni40NTUgODkzLjM5MyA2MDEuMjE1IDg3Ni42MDQgNjMwLjU0OUw2ODcuNTczIDk2NC43MDJMNjg3LjA4NCA5NjUuNTU4QzY3MC40MzYgOTk0LjY5MyA2NjEuOTk5IDEwMDkuNDYgNjUwLjMwNiAxMDIwLjZDNjM3LjU3NiAxMDMyLjc4IDYyMi4yNjMgMTA0MS42MyA2MDUuNDc0IDEwNDYuNjJDNTkwLjE2MSAxMDUwLjg2IDU3My4wMDQgMTA1MC44NiA1MzguNjg4IDEwNTAuODZaTTkwNi43NSAxMDUwLjg2SDExMTUuNTlDMTE0Ni40IDEwNTAuODYgMTE2MS45IDEwNTAuODYgMTE3MS4xMyAxMDQ0Ljc4QzExODEuMDkgMTAzOC4zMiAxMTg3LjM2IDEwMjcuNDMgMTE4Ny45MiAxMDE1LjYzQzExODguNDUgMTAwNS4xIDExODEuMDUgOTkyLjMzIDExNjYuNTUgOTY3LjMwN0MxMTY2LjA1IDk2Ni40NTUgMTE2NS41NSA5NjUuNTg4IDExNjUuMDQgOTY0LjcwNkwxMDYwLjQzIDc4NS43NUwxMDU5LjI0IDc4My43MzVDMTA0NC41NCA3NTguODc3IDEwMzcuMTIgNzQ2LjMyNCAxMDI3LjU5IDc0MS40NzJDMTAxNy4wOCA3MzYuMTIxIDEwMDQuNzEgNzM2LjEyMSA5OTQuMTk5IDc0MS40NzJDOTg0LjYwNSA3NDYuNDUzIDk3Ni44NTcgNzU5LjU1MiA5NjEuNTQ0IDc4NS45MzRMODU3LjMwNiA5NjQuODkxTDg1Ni45NDkgOTY1LjUwN0M4NDEuNjkgOTkxLjg0NyA4MzQuMDY0IDEwMDUuMDEgODM0LjYxNCAxMDE1LjgxQzgzNS4zNTIgMTAyNy42MiA4NDEuNDQgMTAzOC41IDg1MS40MDIgMTA0NC45NkM4NjAuNDQzIDEwNTAuODYgODc1Ljk0IDEwNTAuODYgOTA2Ljc1IDEwNTAuODZaIiBmaWxsPSIjRTg0MTQyIi8+Cjwvc3ZnPgo=" /></a> |  `0x176D1b6c3Fc1db5f7f967Fdc735f8267cCe741F3`
</details>

