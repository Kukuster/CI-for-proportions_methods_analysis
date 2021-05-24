from decimal import Decimal
from typing import List, Literal, Tuple, Union
from matplotlib import pyplot as plt
from matplotlib.colors import LinearSegmentedColormap, Normalize

import numpy as np
from CI_methods_analyser.methods_for_CI_for_diff_betw_two_proportions import Z_test_combined, Z_test_pooled, Z_test_unpooled, Miettinen_and_Nurminen
from CI_methods_analyser.CI_efficacy_diff_betw_two_proportions import CImethodForDiffBetwTwoProportions_efficacyToolkit
from CI_methods_analyser.data_functions import frange
from CI_methods_analyser.CI_efficacy_proportion import CImethodForProportion_efficacyToolkit
from CI_methods_analyser.methods_for_CI_for_proportion import wald_interval, wilson_score_interval



print("""

#=#=#=#=# numpy longdouble (+ *covered*); sum -> np_sum, ceil -> np_ceil, no prop matrix #=#=#=#=#

""")
# z_precisions = (4.06, 4.9)
# for i, z_precision in enumerate(z_precisions):
CI_tests: List[CImethodForDiffBetwTwoProportions_efficacyToolkit] = []

for args in [
    {
        "method": Miettinen_and_Nurminen,
        "method_name": f"Miettinen and Nurminen’s Likelihood Score Test",
        "sample_size1": 100,
        "sample_size2": 100,
        "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.01'))),
        "confidence": 0.95,
        "z_precision": "auto",
    },
    {
        "method": Miettinen_and_Nurminen,
        "method_name": f"Miettinen and Nurminen’s Likelihood Score Test",
        "sample_size1": 200,
        "sample_size2": 200,
        "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.01'))),
        "confidence": 0.95,
        "z_precision": "auto",
    },

    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 100,
    #     "sample_size2": 100,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.035'))),
    #     "confidence": 0.95,
    #     "n_of_experiments": 4000,
    # },
    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 1000,
    #     "sample_size2": 1000,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.035'))),
    #     "confidence": 0.99,
    #     "n_of_experiments": 4000,
    # },
    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 1000,
    #     "sample_size2": 1000,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.035'))),
    #     "confidence": 0.999,
    #     "n_of_experiments": 4000,
    # },
    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 10000,
    #     "sample_size2": 10000,
    #     "proportions": list(frange(Decimal('0.0001'), Decimal('0.0999'), Decimal('0.0075'))),
    #     "confidence": 0.9999,
    #     "z_precision": "auto",
    # },
    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 10000,
    #     "sample_size2": 10000,
    #     "proportions": list(frange(Decimal('0.0001'), Decimal('0.0199'), Decimal('0.0005'))),
    #     "confidence": 0.9999,
    #     "z_precision": 4,
    # },
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 100_000,
    #     "sample_size2": 100_000,
    #     "proportions": list(frange(Decimal('0.00001'), Decimal('0.00999'), Decimal('0.00035'))),
    #     "confidence": 0.99999,
    #     "z_precision": "auto",
    # },
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 1_000_000,
    #     "sample_size2": 1_000_000,
    #     "proportions": list(frange(Decimal('0.000001'), Decimal('0.000999'), Decimal('0.000035'))),
    #     "confidence": 0.999999,
    #     "z_precision": "auto",
    # },
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 10_000_000,
    #     "sample_size2": 10_000_000,
    #     "proportions": list(frange(Decimal('0.0000001'), Decimal('0.0000999'), Decimal('0.0000035'))),
    #     "confidence": 0.9999999,
    #     "z_precision": "auto",
    # },
    ########
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 100_000_000,
    #     "sample_size2": 100_000_000,
    #     "proportions": list(frange(Decimal('0.00000001'), Decimal('0.00000999'), Decimal('0.00000050'))),
    #     "confidence": 0.99999999,
    #     "z_precision": "auto",
    # },
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 100_000_000,
    #     "sample_size2": 100_000_000,
    #     "proportions": list(frange(Decimal('0.00000001'), Decimal('0.00000999'), Decimal('0.00000050'))),
    #     "confidence": 0.99999999,
    #     "z_precision": 8.5,
    # },
    ##########

    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 1000,
    #     "sample_size2": 1000,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.199'), Decimal('0.003'))),
    #     "confidence": 0.95,
    #     "z_precision": "auto",
    # },



    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 100,
    #     "sample_size2": 100,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.199'), Decimal('0.002'))),
    #     "confidence": 0.99
    # },
    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 200,
    #     "sample_size2": 200,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.02'))),
    #     "confidence": 0.95
    # },

    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 10_000_000,
    #     "sample_size2": 10_000_000,
    #     "proportions": list(frange(Decimal('0.0000001'), Decimal('0.0000100'), Decimal('0.0000002'))),
    #     "confidence": 0.9999995,
    # },

    # {
    #     "method": Z_test_unpooled,
    #     "method_name": f"Z test (unpooled)",
    #     "sample_size1": 10_000_000,
    #     "sample_size2": 10_000_000,
    #     "proportions": list(frange(Decimal('0.0000001'), Decimal('0.0000100'), Decimal('0.0000002'))),
    #     "confidence": 0.9999995,
    # },

    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 100,
    #     "sample_size2": 100,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.199'), Decimal('0.002'))),
    #     "confidence": 0.99
    # },
    # {
    #     "method": Z_test_pooled,
    #     "method_name": f"Z test (pooled)",
    #     "sample_size1": 200,
    #     "sample_size2": 200,
    #     "proportions": list(frange(Decimal('0.001'), Decimal('0.999'), Decimal('0.02'))),
    #     "confidence": 0.95
    # },
]:
    CI_test = CImethodForDiffBetwTwoProportions_efficacyToolkit(
        args["method"], args["method_name"])
    
    if "z_precision" in args.keys():
        CI_test.calculate_coverage_analytically(
            sample_size1 = args["sample_size1"],
            sample_size2 = args["sample_size2"],
            proportions  = args["proportions"],
            confidence   = args["confidence"],
            z_precision  = args["z_precision"],
        )
    elif "n_of_experiments" in args.keys():
        CI_test.calculate_coverage_randomly(
            sample_size1=args["sample_size1"],
            sample_size2=args["sample_size2"],
            proportions=args["proportions"],
            confidence=args["confidence"],
            n_of_experiments=args["n_of_experiments"],
        )
    else:
        CI_test.calculate_coverage_analytically(
            sample_size1 = args["sample_size1"],
            sample_size2 = args["sample_size2"],
            proportions  = args["proportions"],
            confidence   = args["confidence"]
        )

    CI_tests.append(CI_test)





########################################
#####                              #####
#####             PLOT             #####
#####                              #####
########################################


for CI_test in CI_tests:
    CI_test.plot_coverage(f'', theme="dark_background")

for CI_test in CI_tests:
    CI_test.show_plot()

# plot_2d_difference(data1=CI_tests[0].coverage,
#           data2=CI_tests[1].coverage,
#           plt_figure_num=f"Z test (unpooled) precision {get_binomial_z_precision(CI_tests[0].confidence)} vs {8}",
#           theme="dark_background").show()

input("Press Enter to exit...")
input("Press Enter to exit...")
input("Press Enter to exit...")
input("Press Enter to exit...")

# CI_method_for_proportion_efficacy.show_plot()
# CI_method_for_diff_betw_two_proportions_efficacy.show_plot()

# CI_by_wald.plot_coverage(theme="dark_background")

# CI_by_wald.show_plot()


