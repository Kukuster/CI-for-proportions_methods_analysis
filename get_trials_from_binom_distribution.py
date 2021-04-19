import numpy as np
import math
from scipy import stats
from scipy.stats import norm
from typing import Callable, Generator, Iterable, List, Tuple, Union, Literal
from functools import lru_cache





def get_trials_from_binom_distribution(n: int, p: float, n_samples: int, randomly: bool = True):
    if randomly:
        return np.random.binomial(n, p, n_samples)
    else:
        # if not randomly, then represent the binomial distribution itself with number of samples = n_samples
        arr = []
        for x in range(0,n+1):
            y_at_x = stats.binom.pmf(x, n, p)
            if y_at_x < 0.0000001:
                continue
            num_of_trials = round(y_at_x*n_samples)
            trials = [x]*num_of_trials
            arr.extend([x]*num_of_trials)
        return np.array(arr)


# ar = get_trials_from_binom_distribution(n=2000, p=0.01, n_samples=20, randomly=False)
# print(sorted(ar), len(ar))
# print("")
# ar = get_trials_from_binom_distribution(n=2000, p=0.01, n_samples=20, randomly=True)
# print(sorted(ar), len(ar))
# ar = get_trials_from_binom_distribution(n=2000, p=0.01, n_samples=20, randomly=True)
# print(sorted(ar), len(ar))
# ar = get_trials_from_binom_distribution(n=2000, p=0.01, n_samples=20, randomly=True)
# print(sorted(ar), len(ar))


print(get_trials_from_binom_distribution(n=20000, p=0.01, n_samples=200, randomly=True))

