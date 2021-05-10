from collections import defaultdict
from decimal import Decimal
from matplotlib.colors import LinearSegmentedColormap, Normalize
import matplotlib.ticker as ticker
from lib.CI_efficacy import CImethod_efficacyToolkit, NoCoverageException
from lib.data_functions import float_to_str
from lib.math_functions import binomial_distribution_two_tailed_range, normal_z_score_two_tailed
from typing import Callable, Generator, Iterable, List, Tuple, Union, Literal
from numpy.random import binomial as binomial_experiment
from scipy.stats import binom as binomial_distribution
from matplotlib import pyplot as plt
import numpy as np
from math import ceil







sample_size = 20
prob_x1 = 0.8
prob_x2 = 0.5

x1_from, x1_to = binomial_distribution_two_tailed_range(n=sample_size, p=prob_x1, sds=4.71)
x2_from, x2_to = binomial_distribution_two_tailed_range(n=sample_size, p=prob_x2, sds=4.71)
# x1s = range(x1_from, x1_to+1)
# x2s = range(x2_from, x2_to+1)
x1s = range(0, sample_size+1)
x2s = range(0, sample_size+1)

y1_sum = sum([binomial_distribution.pmf(x1, sample_size, prob_x1) for x1 in x1s])
y2_sum = sum([binomial_distribution.pmf(x2, sample_size, prob_x2) for x2 in x2s])
print(y1_sum*y2_sum)
assert 0.9999 < y1_sum*y2_sum <= 1.0001

def binom1(x: int) -> float:
    return binomial_distribution.pmf(x, sample_size, prob_x1)

def binom2(x: int) -> float:
    return binomial_distribution.pmf(x, sample_size, prob_x2)

max_x1 = round(prob_x1*sample_size)
max_x2 = round(prob_x2*sample_size)

max_y1 = binom1(max_x1)
max_y2 = binom2(max_x2)

max_point = max_y1*max_y2

print(f"""
max_x1 = {max_x1},
max_x2 = {max_x2},
max_y1 = {max_y1},
max_y2 = {max_y2}
""")
print(max_point)


coverage = np.zeros((len(x1s), len(x2s)), dtype=float)

for i1, x1 in enumerate(x1s):
    for i2, x2 in enumerate(x2s):
        coverage[i1][i2] = binom1(x1)*binom2(x2)/max_point

print(coverage)




def plot_data(
    data: np.ndarray,
    plt_figure_num: Union[str, int],
    theme: Literal["dark_background", "classic", "default"] = "default"
    ):

    plt.style.use(theme)

    # nodes = [0, max_point, 0.1, 1]
    # colors = ["black", "red", "white", "teal"]
    nodes = [0, 0.0001, 0.1, 1]
    colors = ["black", "#3f4f4f", "teal", "white"]
    cmap = LinearSegmentedColormap.from_list("", list(zip(nodes, colors)))
    cmap.set_under("black")

    # plt.matshow(data)
    fig, ax = plt.subplots()
    fig.canvas.set_window_title(str(plt_figure_num))
    im = ax.imshow(data, cmap=cmap, norm=Normalize(0, 1, True))
    fig.colorbar(im, extend="min")


plot_data(coverage, plt_figure_num=1, theme="dark_background")
plot_data(coverage, plt_figure_num=2, theme="classic")
plt.show()
