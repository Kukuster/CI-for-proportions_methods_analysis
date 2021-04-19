# imports
# for 100% precision fractional operations (doesn't support most math functions like sqrt)
from decimal import Decimal
from typing import Callable, Generator, Iterable, List, Tuple, Union, Literal
# for high precision float operations (supports most math functions like sqrt, often faster than decimal)
from bigfloat import BigFloat
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np
import math
# import csv
import pandas as pd
import time
from itertools import product as cartesian_product, permutations
from functools import reduce
from matplotlib.colors import LinearSegmentedColormap, Normalize



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

def zScore_normal(conflevel: float = 0.95):
    z: float = norm.ppf((1+conflevel)/2)
    return abs(z)


### CI METHODS FOR THE DIFFERENCE BETWEEN TWO PROPORTIONS ###

CI_method = Callable[
    [int, int, int, int, Union[float, None], Union[float, None]],
    Tuple[float, float]
]


def wald_interval(xT: int, nT: int, xC: int, nC: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None) -> Tuple[float, float]:
    # LATEX: $$ (\delta^-, \delta^+) = \hat{p}_T - \hat{p}_C \pm z_{\alpha/2}\sqrt{\frac{\hat{p}_T (1 - \hat{p}_T)}{n_T} + \frac{\hat{p}_C (1 - \hat{p}_C)}{n_C}} $$
    """Calculates confidence interval for the difference between two proportions using Wald Interval method

    `xT` - succeeded trials in the experimental (trial) group

    `nT` - total trials in the experimental (trial) group

    `xC` - succeeded trials in the control group

    `nC` - total trials in the control group

    `conflevel` - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset

    `z` - z score. If unset, calculated form the given *conflevel*
    """
    pT = float(xT)/nT
    pC = float(xC)/nC
    if z is None:
        if conflevel is None:
            conflevel = 0.95
        # z = zScore_normal(conflevel)
        conflevel_alphahalved = 1 - ((1 - conflevel)/2) # e.g. 0.95 becomes 0.975
        z = zScore_normal(conflevel_alphahalved)

    delta = pC - pT

    sd = math.sqrt((pT*(1-pT))/nT + (pC*(1-pC))/nC)
    z_sd = abs(z*sd)
    ci = (
        delta - z_sd,
        delta + z_sd
    )
    return ci



### MAIN FUNCTIONS ###

def calculate_coverage(numSamples: int, numTrials: int, probs: Iterable[float], conflevel: float, method: CI_method) -> np.ndarray:
    if not 0 < conflevel < 1:
        raise ValueError(
            f"confidence level has to be real value between 0 and 1. Got: conflevel={conflevel}")

    probs = list(probs)

    # n by n zero matrix, where n is the number of tested probabilities (actual population proportions)
    coverage = np.zeros((len(probs),len(probs)), dtype=float)

    # z = zScore_normal(conflevel)
    conflevel_alphahalved = 1 - ((1 - conflevel)/2) # e.g. 0.95 becomes 0.975
    z = zScore_normal(conflevel_alphahalved)

    # here we get the list of tuples that is the cartesian product of the list *probs* by itself,
    # but there's no need in the entire "matrix":
    #   for every pair (xi, xj) the same result will be used for (xj, xi)
    # therefore, only "left diagonal matrix" elements of this "matrix" have to be generated
    left_diagonal_matrix: np.ndarray = np.zeros((len(probs),len(probs)), dtype=object)
    for i in range(0, len(probs)):
        for j in range(0, i):
            left_diagonal_matrix[i][j] = None
        for j in range(i, len(probs)):
            left_diagonal_matrix[i][j] = (probs[i],probs[j])
    
    # probs_pairs: List[Tuple[float,float]] = []
    # for i in range(0, len(probs)):
    #     for j in range(i, len(probs)):
    #         probs_pairs.append((probs[i],probs[j]))

    # # All tuples are unqiue pairs
    # assert len(list(set([frozenset(e) for e in probs_pairs]))) == len(probs_pairs), \
    #     "The list *probs_pairs* has to have only unique pairs of floats"

    for i in range(0, len(probs)):
        for j in range(0, i):
            pass
        for j in range(i, len(probs)):
            (prob_x, prob_y) = left_diagonal_matrix[i][j]
            
            x = np.random.binomial(numTrials, prob_x, numSamples)
            y = np.random.binomial(numTrials, prob_y, numSamples)
            delta = abs(prob_y - prob_x)
            cis = [method(x[i], numTrials, y[i], numTrials, None, z) for i in range(0, numSamples)]
            covered = [int(ci[0] < delta < ci[1]) for ci in cis]
            thiscoverage = (sum(covered)/numSamples) * 100
            if thiscoverage == 0:
                print([(delta, ci) for ci in cis])
                print(covered)
                exit()
            print(
                f"prob_x = {prob_x:4}; prob_y = {prob_y:4}; coverage ={thiscoverage:6.2f}")
            coverage[i][j] = coverage[j][i] = thiscoverage
    
    # for prob_pair in probs_pairs:
    #     x1 = np.random.binomial(numTrials, prob_pair[0], numSamples)
    #     x2 = np.random.binomial(numTrials, prob_pair[1], numSamples)
    #     delta = abs(prob_pair[1] - prob_pair[0])
    #     cis = [method(x1[i], numTrials, x2[i], numTrials, None, z) for i in range(0, numSamples)]
    #     covered = [int(ci[0] < delta < ci[1]) for ci in cis]
        
    #     # ???
    #     # I have a list of probablilty pair, 
    #     # but I have to get the corresponding i and j indeces to place the results in the diagonally symmetrical matrix
    #     coverage[i][j]


    #     # x = np.random.binomial(numTrials, prob, numSamples)
    #     # cis = [method(x[j], numTrials, None, z) for j in range(0, numSamples)]
    #     # covered = [int(ci[0] < prob < ci[1]) for ci in cis]
    #     # thiscoverage = (sum(covered)/numSamples) * 100
    #     # coverage.append(thiscoverage)
    #     # print(f"prob ={prob:9}; coverage ={thiscoverage:6.2f}")

    return coverage


## just copied from the previous file
## calculate_coverage seems to be done (but not tested)
def plot_coverage(probs: Iterable[float], coverage: np.ndarray, conflevel: float, title: str, xlabel: str, ylabel: str):
    probs = list(probs)

    nodes = [0, max(1-((1-conflevel)/2),0), conflevel, 1.0]
    colors = ["gray", "red", "white", "green"]
    cmap = LinearSegmentedColormap.from_list("", list(zip(nodes, colors)))
    cmap.set_under("gray")

    # plt.matshow(coverage)
    fig, ax = plt.subplots()
    im = ax.imshow(coverage, cmap=cmap, norm=Normalize(0,100,True))
    fig.colorbar(im, extend="min")
    # We want to show all ticks...
    ax.set_xticks(np.arange(len(probs)))
    ax.set_yticks(np.arange(len(probs)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(probs)
    ax.set_yticklabels(probs)





#     plt.plot(list(probs), coverage, color='green',
#              marker=',', linestyle='solid', zorder=5)
#     plt.axhline(conflevel*100, color='orange', linestyle=":", zorder=0)
#     x1, x2, y1, y2 = plt.axis()
#     plt.axis((x1, x2, 50, 100))
#     plt.title(title, fontsize="large", fontweight="bold")
#     plt.xlabel(xlabel)
#     plt.ylabel(ylabel)
#     x1, x2, y1, y2 = plt.axis()

#     avg_deviation = Decimal(0)
#     conflevel_percent = Decimal(conflevel*100)
#     for cov in coverage:
#         deviation = abs(Decimal(cov)-conflevel_percent)
#         # print(f"deviation = {floatToStr(deviation, 2)}")
#         avg_deviation += deviation
#     avg_deviation = avg_deviation/len(coverage)
#     plt.text((x1+x2)/2, (y1+5),
#              f"average deviation from {floatToStr(conflevel*100, 2)}% point = {floatToStr(avg_deviation, 4)} (coverage %)",
#              ha="center", fontstyle="italic", zorder=10)
#     plt.xticks(fontsize=8)
#     plt.ticklabel_format(scilimits=(-3, 3), useMathText=True)


### EXE ###

numSamples = 10000
numTrials = 100
step = Decimal('0.04')
probs = list(frange(Decimal('0.01'), Decimal('0.99'), step))
# probs = list(cartesian_product(probs, probs))
conflevel = 0.95


# print(calculate_coverage(numSamples, numTrials, probs, conflevel, wald_interval))


i = 0
(method, methodname, method_filename) = (wald_interval, "Wald Interval", 'wald')
start_time = time.time()
coverage = calculate_coverage(
    numSamples, numTrials, probs, conflevel, method)
print(coverage)
print("--- %s seconds ---" % (time.time() - start_time))

for (theme, theme_filename) in [
    ("default", ""),
    ("dark_background", "_dark")
]:
    plt.style.use(theme)
    i += 1
    # plt.figure(i)
    plot_coverage(probs, coverage, conflevel, title=f"Coverage of {methodname}\n{numSamples} samples ✕ {numTrials} trials",
                    xlabel="True Proportion (Population Proportion)", ylabel=f"Coverage (%) for {floatToStr(conflevel*100, 2)}%CI")
    # plt.show()
    # plt.savefig(
    #     f"{method_filename}_pfrom{probs[0]}_pto{probs[-1]}_pstep{step}_trials{numTrials}_samples{numSamples}{theme_filename}.png")


plt.show()





# # later we define a set of these sets, and «a set can only contain fronzensets (and not ordinary sets)»
# list_of_twoprobs_sets = [frozenset(e) for e in probs]
# set_of_twoprobs_sets = set(list_of_twoprobs_sets)
# list_of_unique_twoprobs_sets = list(set_of_twoprobs_sets)

# print(list_of_unique_twoprobs_sets)
# print(len(list_of_unique_twoprobs_sets))

# lengths_of_sets = [len(s) for s in list_of_unique_twoprobs_sets]
# # avg_length_of_sets = sum(lengths_of_sets)/len(lengths_of_sets)
# print(sum(lengths_of_sets))


# # get the list of tuples that is the cartesian product of the list *probs* by itself
# # but there's no need in the entire "matrix":
# # for every pair (xi, xj) the same result will be used for (xj, xi)
# # therefore, only "left diagonal matrix" elements of this "matrix" have to be generated
# # left_diagonal_matrix: List[List[Tuple[float,float]]] = []
# left_diagonal_matrix = np.zeros((len(probs),len(probs)))
# for i in range(0, len(probs)):
#     for j in range(0, i):
#         # here add None to the square matrix
#         pass
#     for j in range(i, len(probs)):
#         left_diagonal_matrix.append((probs[i],probs[j]))

# # print(left_diagonal_matrix)
# print(len(left_diagonal_matrix))

# # All tuples are unqiue pairs
# assert len(list(set([frozenset(e) for e in left_diagonal_matrix]))) == len(left_diagonal_matrix), "The list *left_diagonal_matrix* has to have only unique pairs of floats"



# unique_probs = [tuple(e) for e in twoprobs_sets]
# # print(probs)
# print(unique_probs)
# # print(len(probs))
# print(len(unique_probs))

