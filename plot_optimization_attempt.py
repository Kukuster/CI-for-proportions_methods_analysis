# imports
# for 100% precision fractional operations (doesn't support most math functions like sqrt)
from decimal import Decimal
from typing import Callable, Generator, Iterable, List, Tuple, Union, Literal
# for high precision float operations (supports most math functions like sqrt, often faster than decimal)
from bigfloat import BigFloat, sqrt
from matplotlib import pyplot as plt
from scipy.stats import norm
import numpy as np
from math import sqrt
import time


### FORMATTING FUNCTIONS ###

def floatToStr(inputValue: Union[float, BigFloat, Decimal], precision: int = 10):
    return (f'%.{precision}f' % inputValue).rstrip('0').rstrip('.')


### DATA FUNCTIONS ###

# like python range, but for floats
def frange(x: Union[float, Decimal], y: Union[float, Decimal], jump: Union[float, Decimal]) -> Generator[float, None, None]:
    while x <= y:
        yield float(x)
        x = Decimal(x) + Decimal(jump)


### MATH FUNCTIONS ###

def zScore_normal(conflevel: float = 0.95):
    z: float = norm.ppf((1+conflevel)/2)
    return abs(z)


### CI METHODS FOR PROPORTIONS ###

CI_method = Callable[
    [int, int, Union[float, None], Union[float, None]],
    Tuple[float, float]
]


# x - succeeded trials
# n - total trials
# conflevel - confidence level (0 < float < 1). Defaults to 0.95 if its unset and *z* is unset
# z - z score. If unset, calculated form the given *conflevel*
    # LaTeX: $$(w^-, w^+) = \hat{p}\,\pm\,z\sqrt{\frac{\hat{p}(1-\hat{p})}{n}}$$
def wald_interval(x, n: int, conflevel: Union[float, None] = 0.95, z: Union[float, None] = None):
    p = x/n

    sd = sqrt((p*(1-p))/n)
    # sd = 0.001
    z_by_sd = z*sd
    ci = (
        p - z_by_sd,
        p + z_by_sd
    )
    return ci
    return (0.3, 0.7)



numSamples = 10000
numTrials = 100
step = Decimal('0.01')
probs = list(frange(Decimal('0.001'), Decimal('0.999'), step))
conflevel = 0.95

coverage = []
z = zScore_normal(conflevel)

# ci: Tuple[float, float]
start_time = time.time()
for prob in probs:
    # binomgen_start_time = time.time()
    x = np.random.binomial(numTrials, prob, numSamples)
    # binomgen_end_time = time.time() - binomgen_start_time
    # binomgen_exe_time_str = f"{binomgen_end_time:6.5f} s"
    # n_covered = 0
    # covered = []
    # covcalc_start_time = time.time()
    # for j in range(0, numSamples):
    #     ci = wald_interval(x[j], numTrials, None, z)
    #     n_covered += int(ci[0] < prob < ci[1])
        # covered.append(int(ci[0] < prob < ci[1]))
    # n_covered = sum(covered)
    # cis_start_time = time.time()
    cis = [wald_interval(float(x[j]), numTrials, None, z) for j in range(0, numSamples)]
    # cis_end_time = time.time() - cis_start_time
    # cis_exe_time_str = f"{cis_end_time:6.5f} s"
    # cov_start_time = time.time()
    covered = [int(ci[0] < prob < ci[1]) for ci in cis]
    # cov_end_time = time.time() - cov_start_time
    # cov_exe_time_str = f"{cov_end_time:6.5f} s"
    # covcalc_end_time = time.time() - covcalc_start_time
    # covcalc_exe_time_str = f"{covcalc_end_time:9.5f} s"
    # captures the coverage for each of the true proportions. Ideally, for a 95%CI this should be more or less 95%
    # thiscoverage = (n_covered/numSamples) * 100
    # thiscoverage = (sum(covered)/numSamples) * 100
    coverage.append(covered)
    # print(f"prob ={prob:7}; coverage ={thiscoverage:6.2f}; binomgentime = {binomgen_exe_time_str}; cistime = {cis_exe_time_str}; covtime = {cov_exe_time_str}; ")
    # print(f"prob ={prob:7}; coverage ={thiscoverage:6.2f}; binomgentime = {binomgen_exe_time_str}; cistime = {cis_exe_time_str}; covtime = {cov_exe_time_str}; ")
    # print(f"prob ={prob:7}; coverage ={thiscoverage:6.2f}; binomgentime = {binomgen_exe_time_str}; covcalctime = {covcalc_exe_time_str}")
    # print(f"prob ={prob:7}; coverage ={thiscoverage:6.2f}")
coverage = [(sum(covered)/numSamples)*100 for covered in coverage]
print("--- %s seconds ---" % (time.time() - start_time))

plt.plot(list(probs), coverage, color='green', marker=',', linestyle='solid', zorder=5)
plt.axhline(conflevel*100, color='orange', linestyle=":", zorder=0)
x1, x2, y1, y2 = plt.axis()
plt.axis((x1, x2, 50, 100))
plt.title(f"Coverage of Wald Interval\n{numSamples} samples ✕ {numTrials} trials",
          fontsize="large", fontweight="bold")
plt.xlabel("True Proportion (Population Proportion)")
plt.ylabel(f"Coverage (%) for {floatToStr(conflevel*100, 2)}%CI")
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
plt.ticklabel_format(scilimits=(-3, 3), useMathText=True)
plt.show()
