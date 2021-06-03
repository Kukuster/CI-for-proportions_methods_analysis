from CI_methods_analyser.math_functions import normal_z_score_two_tailed
from math import sqrt as math_sqrt
from functools import lru_cache


from CI_methods_analyser import *


@lru_cache(100_000)
def wald_interval(x: int, n: int, conflevel: float = 0.95):
    """Calculates confidence interval for proportions

    `x` - succeeded trials

    `n` - total trials

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    if x > n:
        raise ValueError(f"Number of succeeded trials (x) has to be no more than number of total trials (n). x = {x} and n = {n} were passed")

    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    sd = math_sqrt((p*(1-p))/n)
    z_sd = z*sd
    ci = (
        p - z_sd,
        p + z_sd
    )
    return ci


@lru_cache(100_000)
def a_method(x: int, n: int, conflevel: float = 0.95):
    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    return (
        (0 + 3*p)/4 - 0.02,
        (3*p + 1)/4 + 0.02
    )


@lru_cache(100_000)
def im_telling_ya_method(x: int, n: int, conflevel: float = 0.95):
    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    return (
        p - 0.01,
        p + 0.01
    )


@lru_cache(100_000)
def God_is_the_witness_method(x: int, n: int, conflevel: float = 0.95):
    z = normal_z_score_two_tailed(conflevel)

    p = float(x)/n
    return (
        (0 + p)/2 - 0.02,
        (1 + p)/2 + 0.02
    )


# CImethodForProportion_efficacyToolkit(
#     method=a_method,
#     method_name="Mustache interval"
# ).calculate_coverage_and_show_plot(
#     sample_size=100,
#     proportions=('0.001', '0.999', '0.001'),
#     confidence=0.90,
#     theme="dark_background",plt_figure_title="Mustache interval"
# )

# CImethodForProportion_efficacyToolkit(
#     method=im_telling_ya_method,
#     method_name="I'm telling ya test"
# ).calculate_coverage_and_show_plot(
#     sample_size=100,
#     proportions=('0.001', '0.999', '0.001'),
#     confidence=0.90,
#     theme="dark_background",plt_figure_title="I'm telling ya test"
# )

CImethodForProportion_efficacyToolkit(
    method=God_is_the_witness_method,
    method_name="\"God is the witness\" score"
).calculate_coverage_and_show_plot(
    sample_size=100,
    proportions=('0.001', '0.999', '0.001'),
    confidence=0.90,
    theme="dark_background", plt_figure_title="\"God is the witness\" score"
)



input("Press enter to exit")

