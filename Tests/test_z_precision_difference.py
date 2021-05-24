"""
A test that validates that automatically optimized approximation to the analytical solution
to the real coverage doesn't deviate from precise analytical solution to any significant degree.

See:
 • "efficacy of an arbitrary CI method for proportions - analytical solution.jpg"

 • "CI_efficacy_proportion.py".
      CImethodForProportion_efficacyToolkit.calculate_coverage_analytically()

 • "CI_efficacy_diff_betw_two_proportions.py".
      CImethodForDiffBetwTwoProportions_efficacyToolkit.calculate_coverage_analytically()

"""
import time

import numpy as np

from CI_methods_analyser.data_functions import float_to_str
from CI_methods_analyser.CI_efficacy_proportion import CImethodForProportion_efficacyToolkit
from CI_methods_analyser.methods_for_CI_for_proportion import wald_interval, wilson_score_interval
from Tests.plot_difference import plot_relative_difference




"""
Comparing to z_precision=9 as the maximum precision. Why 9?

https://www.wolframalpha.com/input/?i=9+sigmas

9 sigmas two-tailed p-value is 2e-19, which is just 2 times more than 
the maximum precision of units in mantissa given by 63 bits for mantissa in np.float128:
it's almost 1 in 1e19, which is sensitivty of 1e-19 per unit.

It means that the values outside 9 sigmas all add up to about 2e-19.
Therefore the individual `y` values of a given binomial distribution outside 9 sigmas
don't exceed 2e-19, and only values of at least 1e-19 can be added to a np.float128 value 
of approximately from 0.5 to 0.9999999...

Thus, z_precision of 9 behaves here just like a maximum precision.
"""

print("")
print("===== CI test1 ======")
print("")

start_time = time.time()

proportions = ('0.001', '0.999', '0.003')

CI_test_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_1_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.90)

CI_test_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_1b_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.90)

CI_test_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_1_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.90, z_precision=9)

CI_test_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_1b_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.90, z_precision=9)



CI_test_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_2_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.95)

CI_test_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_2b_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.95)

CI_test_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_2_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.95, z_precision=9)

CI_test_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_2b_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.95, z_precision=9)



CI_test_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_3_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.99)

CI_test_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_3b_auto.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.99)

CI_test_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_3_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.99, z_precision=9)

CI_test_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_3b_max.calculate_coverage_analytically(
    sample_size=100, proportions=proportions, confidence=0.99, z_precision=9)



CI_test_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_4_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.90)

CI_test_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_4b_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.90)

CI_test_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_4_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.90, z_precision=9)

CI_test_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_4b_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.90, z_precision=9)



CI_test_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_5_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.95)

CI_test_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_5b_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.95)

CI_test_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_5_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.95, z_precision=9)

CI_test_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_5b_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.95, z_precision=9)



CI_test_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_6_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.99)

CI_test_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_6b_auto.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.99)

CI_test_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test_6_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test_6b_max.calculate_coverage_analytically(
    sample_size=1000, proportions=proportions, confidence=0.99, z_precision=9)

print("CI test1 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))

print("")
print("===== CI test2 ======")
print("")

start_time = time.time()

proportions = ('0.00001', '0.00999', '0.00004')




CI_test2_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_1_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.90)

CI_test2_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_1b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.90)

CI_test2_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_1_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.90, z_precision=9)

CI_test2_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_1b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.90, z_precision=9)



CI_test2_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_2_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.95)

CI_test2_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_2b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.95)

CI_test2_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_2_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.95, z_precision=9)

CI_test2_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_2b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.95, z_precision=9)



CI_test2_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_3_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99)

CI_test2_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_3b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99)

CI_test2_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_3_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test2_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_3b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99, z_precision=9)



CI_test2_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_4_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.90)

CI_test2_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_4b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.90)

CI_test2_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_4_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.90, z_precision=9)

CI_test2_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_4b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.90, z_precision=9)



CI_test2_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_5_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95)

CI_test2_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_5b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95)

CI_test2_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_5_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95, z_precision=9)

CI_test2_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_5b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95, z_precision=9)



CI_test2_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_6_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test2_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_6b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test2_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test2_6_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test2_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test2_6b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)

print("CI test2 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))

print("")
print("===== CI test3 ======")
print("")

start_time = time.time()


proportions = ('0.000001', '0.000999', '0.000004')




CI_test3_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_1_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99)

CI_test3_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_1b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99)

CI_test3_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_1_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test3_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_1b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.99, z_precision=9)



CI_test3_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_2_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.995)

CI_test3_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_2b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.995)

CI_test3_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_2_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.995, z_precision=9)

CI_test3_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_2b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.995, z_precision=9)



CI_test3_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_3_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.999)

CI_test3_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_3b_auto.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.999)

CI_test3_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_3_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test3_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_3b_max.calculate_coverage_analytically(
    sample_size=10000, proportions=proportions, confidence=0.999, z_precision=9)



CI_test3_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_4_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test3_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_4b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test3_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_4_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test3_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_4b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)



CI_test3_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_5_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.995)

CI_test3_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_5b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.995)

CI_test3_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_5_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.995, z_precision=9)

CI_test3_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_5b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.995, z_precision=9)



CI_test3_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_6_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test3_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_6b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test3_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test3_6_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test3_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test3_6b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)

print("CI test3 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))

print("")
print("===== CI test4 ======")
print("")

start_time = time.time()

proportions = ('0.000001', '0.000999', '0.000007')




CI_test4_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_1_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test4_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_1b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test4_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_1_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test4_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_1b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)



CI_test4_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_2_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9995)

CI_test4_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_2b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9995)

CI_test4_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_2_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9995, z_precision=9)

CI_test4_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_2b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9995, z_precision=9)



CI_test4_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_3_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9999)

CI_test4_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_3b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9999)

CI_test4_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_3_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9999, z_precision=9)

CI_test4_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_3b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.9999, z_precision=9)



CI_test4_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_4_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999)

CI_test4_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_4b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999)

CI_test4_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_4_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test4_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_4b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999, z_precision=9)



CI_test4_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_5_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9995)

CI_test4_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_5b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9995)

CI_test4_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_5_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9995, z_precision=9)

CI_test4_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_5b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9995, z_precision=9)



CI_test4_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_6_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9999)

CI_test4_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_6b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9999)

CI_test4_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test4_6_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9999, z_precision=9)

CI_test4_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test4_6b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.9999, z_precision=9)

print("CI test4 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))

print("")
print("===== CI test5 ======")
print("")

start_time = time.time()

proportions = ('0.0000001', '0.0000199', '0.0000002')



CI_test5_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_1_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test5_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_1b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test5_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_1_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test5_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_1b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test5_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_2_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test5_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_2b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test5_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_2_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test5_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_2b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test5_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_3_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test5_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_3b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test5_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_3_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test5_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_3b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)



CI_test5_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_4_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test5_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_4b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test5_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_4_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test5_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_4b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test5_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_5_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test5_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_5b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test5_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_5_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test5_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_5b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test5_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_6_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test5_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_6b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test5_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test5_6_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test5_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test5_6b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

print("CI test5 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))

print("")
print("===== CI test6 ======")
print("")

start_time = time.time()

proportions = ('0.0000001', '0.0001999', '0.0000011')



CI_test6_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_1_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test6_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_1b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test6_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_1_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test6_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_1b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test6_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_2_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test6_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_2b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test6_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_2_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test6_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_2b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test6_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_3_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test6_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_3b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test6_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_3_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test6_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_3b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)



CI_test6_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_4_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test6_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_4b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test6_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_4_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test6_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_4b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test6_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_5_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test6_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_5b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test6_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_5_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test6_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_5b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test6_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_6_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test6_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_6b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test6_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test6_6_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test6_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test6_6b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

print("CI test6 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))



print("")
print("===== CI test7 ======")
print("")

start_time = time.time()

proportions = ('0.0001', '0.1999', '0.0019')



CI_test7_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_1_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test7_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_1b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999)

CI_test7_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_1_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test7_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_1b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test7_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_2_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test7_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_2b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995)

CI_test7_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_2_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test7_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_2b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test7_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_3_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test7_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_3b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999)

CI_test7_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_3_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test7_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_3b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999999, z_precision=9)



CI_test7_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_4_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test7_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_4b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999)

CI_test7_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_4_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)

CI_test7_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_4b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99999, z_precision=9)



CI_test7_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_5_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test7_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_5b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995)

CI_test7_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_5_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)

CI_test7_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_5b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999995, z_precision=9)



CI_test7_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_6_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test7_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_6b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999)

CI_test7_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test7_6_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

CI_test7_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test7_6b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999999, z_precision=9)

print("CI test7 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))





print("")
print("===== CI test8 ======")
print("")

start_time = time.time()

proportions = ('0.0001', '0.1999', '0.0019')



CI_test8_1_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_1_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95)

CI_test8_1b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_1b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95)

CI_test8_1_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_1_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95, z_precision=9)

CI_test8_1b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_1b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.95, z_precision=9)



CI_test8_2_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_2_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test8_2b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_2b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99)

CI_test8_2_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_2_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test8_2b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_2b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.99, z_precision=9)



CI_test8_3_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_3_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test8_3b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_3b_auto.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999)

CI_test8_3_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_3_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test8_3b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_3b_max.calculate_coverage_analytically(
    sample_size=100000, proportions=proportions, confidence=0.999, z_precision=9)



CI_test8_4_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_4_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.95)

CI_test8_4b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_4b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.95)

CI_test8_4_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_4_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.95, z_precision=9)

CI_test8_4b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_4b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.95, z_precision=9)



CI_test8_5_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_5_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99)

CI_test8_5b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_5b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99)

CI_test8_5_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_5_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99, z_precision=9)

CI_test8_5b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_5b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.99, z_precision=9)



CI_test8_6_auto = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_6_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999)

CI_test8_6b_auto = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_6b_auto.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999)

CI_test8_6_max = CImethodForProportion_efficacyToolkit(wald_interval, "Wald Interval")
CI_test8_6_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999, z_precision=9)

CI_test8_6b_max = CImethodForProportion_efficacyToolkit(wilson_score_interval, "Wilson Score Interval")
CI_test8_6b_max.calculate_coverage_analytically(
    sample_size=1000000, proportions=proportions, confidence=0.999, z_precision=9)

print("CI test8 finished")
print("--- %s seconds ---" % float_to_str((time.time() - start_time), 5))










test_fig1  = plot_relative_difference(
    np.array(CI_test_1_auto.coverage), np.array(CI_test_1_max.coverage),
    plt_figure_num="CI test 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_1_auto.f.calculation_inputs()}")
test_fig1b = plot_relative_difference(
    np.array(CI_test_1b_auto.coverage), np.array(CI_test_1b_max.coverage),
    plt_figure_num="CI test 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_1b_auto.f.calculation_inputs()}")
test_fig2  = plot_relative_difference(
    np.array(CI_test_2_auto.coverage), np.array(CI_test_2_max.coverage),
    plt_figure_num="CI test 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_2_auto.f.calculation_inputs()}")
test_fig2b = plot_relative_difference(
    np.array(CI_test_2b_auto.coverage), np.array(CI_test_2b_max.coverage),
    plt_figure_num="CI test 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_2b_auto.f.calculation_inputs()}")
test_fig3  = plot_relative_difference(
    np.array(CI_test_3_auto.coverage), np.array(CI_test_3_max.coverage),
    plt_figure_num="CI test 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_3_auto.f.calculation_inputs()}")
test_fig3b = plot_relative_difference(
    np.array(CI_test_3b_auto.coverage), np.array(CI_test_3b_max.coverage),
    plt_figure_num="CI test 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_3b_auto.f.calculation_inputs()}")
test_fig4  = plot_relative_difference(
    np.array(CI_test_4_auto.coverage), np.array(CI_test_4_max.coverage),
    plt_figure_num="CI test 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_4_auto.f.calculation_inputs()}")
test_fig4b = plot_relative_difference(
    np.array(CI_test_4b_auto.coverage), np.array(CI_test_4b_max.coverage),
    plt_figure_num="CI test 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_4b_auto.f.calculation_inputs()}")
test_fig5  = plot_relative_difference(
    np.array(CI_test_5_auto.coverage), np.array(CI_test_5_max.coverage),
    plt_figure_num="CI test 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_5_auto.f.calculation_inputs()}")
test_fig5b = plot_relative_difference(
    np.array(CI_test_5b_auto.coverage), np.array(CI_test_5b_max.coverage),
    plt_figure_num="CI test 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_5b_auto.f.calculation_inputs()}")
test_fig6  = plot_relative_difference(
    np.array(CI_test_6_auto.coverage), np.array(CI_test_6_max.coverage),
    plt_figure_num="CI test 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_6_auto.f.calculation_inputs()}")
test_fig6b = plot_relative_difference(
    np.array(CI_test_6b_auto.coverage), np.array(CI_test_6b_max.coverage),
    plt_figure_num="CI test 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test_6b_auto.f.calculation_inputs()}")


test2_fig1  = plot_relative_difference(
    np.array(CI_test2_1_auto.coverage), np.array(CI_test2_1_max.coverage),
    plt_figure_num="CI test2 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_1_auto.f.calculation_inputs()}")
test2_fig1b = plot_relative_difference(
    np.array(CI_test2_1b_auto.coverage), np.array(CI_test2_1b_max.coverage),
    plt_figure_num="CI test2 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_1b_auto.f.calculation_inputs()}")
test2_fig2  = plot_relative_difference(
    np.array(CI_test2_2_auto.coverage), np.array(CI_test2_2_max.coverage),
    plt_figure_num="CI test2 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_2_auto.f.calculation_inputs()}")
test2_fig2b = plot_relative_difference(
    np.array(CI_test2_2b_auto.coverage), np.array(CI_test2_2b_max.coverage),
    plt_figure_num="CI test2 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_2b_auto.f.calculation_inputs()}")
test2_fig3  = plot_relative_difference(
    np.array(CI_test2_3_auto.coverage), np.array(CI_test2_3_max.coverage),
    plt_figure_num="CI test2 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_3_auto.f.calculation_inputs()}")
test2_fig3b = plot_relative_difference(
    np.array(CI_test2_3b_auto.coverage), np.array(CI_test2_3b_max.coverage),
    plt_figure_num="CI test2 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_3b_auto.f.calculation_inputs()}")
test2_fig4  = plot_relative_difference(
    np.array(CI_test2_4_auto.coverage), np.array(CI_test2_4_max.coverage),
    plt_figure_num="CI test2 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_4_auto.f.calculation_inputs()}")
test2_fig4b = plot_relative_difference(
    np.array(CI_test2_4b_auto.coverage), np.array(CI_test2_4b_max.coverage),
    plt_figure_num="CI test2 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_4b_auto.f.calculation_inputs()}")
test2_fig5  = plot_relative_difference(
    np.array(CI_test2_5_auto.coverage), np.array(CI_test2_5_max.coverage),
    plt_figure_num="CI test2 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_5_auto.f.calculation_inputs()}")
test2_fig5b = plot_relative_difference(
    np.array(CI_test2_5b_auto.coverage), np.array(CI_test2_5b_max.coverage),
    plt_figure_num="CI test2 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_5b_auto.f.calculation_inputs()}")
test2_fig6  = plot_relative_difference(
    np.array(CI_test2_6_auto.coverage), np.array(CI_test2_6_max.coverage),
    plt_figure_num="CI test2 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_6_auto.f.calculation_inputs()}")
test2_fig6b = plot_relative_difference(
    np.array(CI_test2_6b_auto.coverage), np.array(CI_test2_6b_max.coverage),
    plt_figure_num="CI test2 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test2_6b_auto.f.calculation_inputs()}")


test3_fig1  = plot_relative_difference(
    np.array(CI_test3_1_auto.coverage), np.array(CI_test3_1_max.coverage),
    plt_figure_num="CI test3 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_1_auto.f.calculation_inputs()}")
test3_fig1b = plot_relative_difference(
    np.array(CI_test3_1b_auto.coverage), np.array(CI_test3_1b_max.coverage),
    plt_figure_num="CI test3 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_1b_auto.f.calculation_inputs()}")
test3_fig2  = plot_relative_difference(
    np.array(CI_test3_2_auto.coverage), np.array(CI_test3_2_max.coverage),
    plt_figure_num="CI test3 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_2_auto.f.calculation_inputs()}")
test3_fig2b = plot_relative_difference(
    np.array(CI_test3_2b_auto.coverage), np.array(CI_test3_2b_max.coverage),
    plt_figure_num="CI test3 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_2b_auto.f.calculation_inputs()}")
test3_fig3  = plot_relative_difference(
    np.array(CI_test3_3_auto.coverage), np.array(CI_test3_3_max.coverage),
    plt_figure_num="CI test3 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_3_auto.f.calculation_inputs()}")
test3_fig3b = plot_relative_difference(
    np.array(CI_test3_3b_auto.coverage), np.array(CI_test3_3b_max.coverage),
    plt_figure_num="CI test3 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_3b_auto.f.calculation_inputs()}")
test3_fig4  = plot_relative_difference(
    np.array(CI_test3_4_auto.coverage), np.array(CI_test3_4_max.coverage),
    plt_figure_num="CI test3 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_4_auto.f.calculation_inputs()}")
test3_fig4b = plot_relative_difference(
    np.array(CI_test3_4b_auto.coverage), np.array(CI_test3_4b_max.coverage),
    plt_figure_num="CI test3 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_4b_auto.f.calculation_inputs()}")
test3_fig5  = plot_relative_difference(
    np.array(CI_test3_5_auto.coverage), np.array(CI_test3_5_max.coverage),
    plt_figure_num="CI test3 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_5_auto.f.calculation_inputs()}")
test3_fig5b = plot_relative_difference(
    np.array(CI_test3_5b_auto.coverage), np.array(CI_test3_5b_max.coverage),
    plt_figure_num="CI test3 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_5b_auto.f.calculation_inputs()}")
test3_fig6  = plot_relative_difference(
    np.array(CI_test3_6_auto.coverage), np.array(CI_test3_6_max.coverage),
    plt_figure_num="CI test3 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_6_auto.f.calculation_inputs()}")
test3_fig6b = plot_relative_difference(
    np.array(CI_test3_6b_auto.coverage), np.array(CI_test3_6b_max.coverage),
    plt_figure_num="CI test3 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test3_6b_auto.f.calculation_inputs()}")


test4_fig1  = plot_relative_difference(
    np.array(CI_test4_1_auto.coverage), np.array(CI_test4_1_max.coverage),
    plt_figure_num="CI test4 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_1_auto.f.calculation_inputs()}")
test4_fig1b = plot_relative_difference(
    np.array(CI_test4_1b_auto.coverage), np.array(CI_test4_1b_max.coverage),
    plt_figure_num="CI test4 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_1b_auto.f.calculation_inputs()}")
test4_fig2  = plot_relative_difference(
    np.array(CI_test4_2_auto.coverage), np.array(CI_test4_2_max.coverage),
    plt_figure_num="CI test4 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_2_auto.f.calculation_inputs()}")
test4_fig2b = plot_relative_difference(
    np.array(CI_test4_2b_auto.coverage), np.array(CI_test4_2b_max.coverage),
    plt_figure_num="CI test4 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_2b_auto.f.calculation_inputs()}")
test4_fig3  = plot_relative_difference(
    np.array(CI_test4_3_auto.coverage), np.array(CI_test4_3_max.coverage),
    plt_figure_num="CI test4 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_3_auto.f.calculation_inputs()}")
test4_fig3b = plot_relative_difference(
    np.array(CI_test4_3b_auto.coverage), np.array(CI_test4_3b_max.coverage),
    plt_figure_num="CI test4 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_3b_auto.f.calculation_inputs()}")
test4_fig4  = plot_relative_difference(
    np.array(CI_test4_4_auto.coverage), np.array(CI_test4_4_max.coverage),
    plt_figure_num="CI test4 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_4_auto.f.calculation_inputs()}")
test4_fig4b = plot_relative_difference(
    np.array(CI_test4_4b_auto.coverage), np.array(CI_test4_4b_max.coverage),
    plt_figure_num="CI test4 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_4b_auto.f.calculation_inputs()}")
test4_fig5  = plot_relative_difference(
    np.array(CI_test4_5_auto.coverage), np.array(CI_test4_5_max.coverage),
    plt_figure_num="CI test4 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_5_auto.f.calculation_inputs()}")
test4_fig5b = plot_relative_difference(
    np.array(CI_test4_5b_auto.coverage), np.array(CI_test4_5b_max.coverage),
    plt_figure_num="CI test4 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_5b_auto.f.calculation_inputs()}")
test4_fig6  = plot_relative_difference(
    np.array(CI_test4_6_auto.coverage), np.array(CI_test4_6_max.coverage),
    plt_figure_num="CI test4 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_6_auto.f.calculation_inputs()}")
test4_fig6b = plot_relative_difference(
    np.array(CI_test4_6b_auto.coverage), np.array(CI_test4_6b_max.coverage),
    plt_figure_num="CI test4 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test4_6b_auto.f.calculation_inputs()}")


test5_fig1  = plot_relative_difference(
    np.array(CI_test5_1_auto.coverage), np.array(CI_test5_1_max.coverage),
    plt_figure_num="CI test5 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_1_auto.f.calculation_inputs()}")
test5_fig1b = plot_relative_difference(
    np.array(CI_test5_1b_auto.coverage), np.array(CI_test5_1b_max.coverage),
    plt_figure_num="CI test5 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_1b_auto.f.calculation_inputs()}")
test5_fig2  = plot_relative_difference(
    np.array(CI_test5_2_auto.coverage), np.array(CI_test5_2_max.coverage),
    plt_figure_num="CI test5 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_2_auto.f.calculation_inputs()}")
test5_fig2b = plot_relative_difference(
    np.array(CI_test5_2b_auto.coverage), np.array(CI_test5_2b_max.coverage),
    plt_figure_num="CI test5 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_2b_auto.f.calculation_inputs()}")
test5_fig3  = plot_relative_difference(
    np.array(CI_test5_3_auto.coverage), np.array(CI_test5_3_max.coverage),
    plt_figure_num="CI test5 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_3_auto.f.calculation_inputs()}")
test5_fig3b = plot_relative_difference(
    np.array(CI_test5_3b_auto.coverage), np.array(CI_test5_3b_max.coverage),
    plt_figure_num="CI test5 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_3b_auto.f.calculation_inputs()}")
test5_fig4  = plot_relative_difference(
    np.array(CI_test5_4_auto.coverage), np.array(CI_test5_4_max.coverage),
    plt_figure_num="CI test5 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_4_auto.f.calculation_inputs()}")
test5_fig4b = plot_relative_difference(
    np.array(CI_test5_4b_auto.coverage), np.array(CI_test5_4b_max.coverage),
    plt_figure_num="CI test5 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_4b_auto.f.calculation_inputs()}")
test5_fig5  = plot_relative_difference(
    np.array(CI_test5_5_auto.coverage), np.array(CI_test5_5_max.coverage),
    plt_figure_num="CI test5 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_5_auto.f.calculation_inputs()}")
test5_fig5b = plot_relative_difference(
    np.array(CI_test5_5b_auto.coverage), np.array(CI_test5_5b_max.coverage),
    plt_figure_num="CI test5 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_5b_auto.f.calculation_inputs()}")
test5_fig6  = plot_relative_difference(
    np.array(CI_test5_6_auto.coverage), np.array(CI_test5_6_max.coverage),
    plt_figure_num="CI test5 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_6_auto.f.calculation_inputs()}")
test5_fig6b = plot_relative_difference(
    np.array(CI_test5_6b_auto.coverage), np.array(CI_test5_6b_max.coverage),
    plt_figure_num="CI test5 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test5_6b_auto.f.calculation_inputs()}")


test6_fig1  = plot_relative_difference(
    np.array(CI_test6_1_auto.coverage), np.array(CI_test6_1_max.coverage),
    plt_figure_num="CI test6 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_1_auto.f.calculation_inputs()}")
test6_fig1b = plot_relative_difference(
    np.array(CI_test6_1b_auto.coverage), np.array(CI_test6_1b_max.coverage),
    plt_figure_num="CI test6 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_1b_auto.f.calculation_inputs()}")
test6_fig2  = plot_relative_difference(
    np.array(CI_test6_2_auto.coverage), np.array(CI_test6_2_max.coverage),
    plt_figure_num="CI test6 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_2_auto.f.calculation_inputs()}")
test6_fig2b = plot_relative_difference(
    np.array(CI_test6_2b_auto.coverage), np.array(CI_test6_2b_max.coverage),
    plt_figure_num="CI test6 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_2b_auto.f.calculation_inputs()}")
test6_fig3  = plot_relative_difference(
    np.array(CI_test6_3_auto.coverage), np.array(CI_test6_3_max.coverage),
    plt_figure_num="CI test6 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_3_auto.f.calculation_inputs()}")
test6_fig3b = plot_relative_difference(
    np.array(CI_test6_3b_auto.coverage), np.array(CI_test6_3b_max.coverage),
    plt_figure_num="CI test6 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_3b_auto.f.calculation_inputs()}")
test6_fig4  = plot_relative_difference(
    np.array(CI_test6_4_auto.coverage), np.array(CI_test6_4_max.coverage),
    plt_figure_num="CI test6 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_4_auto.f.calculation_inputs()}")
test6_fig4b = plot_relative_difference(
    np.array(CI_test6_4b_auto.coverage), np.array(CI_test6_4b_max.coverage),
    plt_figure_num="CI test6 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_4b_auto.f.calculation_inputs()}")
test6_fig5  = plot_relative_difference(
    np.array(CI_test6_5_auto.coverage), np.array(CI_test6_5_max.coverage),
    plt_figure_num="CI test6 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_5_auto.f.calculation_inputs()}")
test6_fig5b = plot_relative_difference(
    np.array(CI_test6_5b_auto.coverage), np.array(CI_test6_5b_max.coverage),
    plt_figure_num="CI test6 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_5b_auto.f.calculation_inputs()}")
test6_fig6  = plot_relative_difference(
    np.array(CI_test6_6_auto.coverage), np.array(CI_test6_6_max.coverage),
    plt_figure_num="CI test6 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_6_auto.f.calculation_inputs()}")
test6_fig6b = plot_relative_difference(
    np.array(CI_test6_6b_auto.coverage), np.array(CI_test6_6b_max.coverage),
    plt_figure_num="CI test6 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test6_6b_auto.f.calculation_inputs()}")


test7_fig1  = plot_relative_difference(
    np.array(CI_test7_1_auto.coverage), np.array(CI_test7_1_max.coverage),
    plt_figure_num="CI test7 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_1_auto.f.calculation_inputs()}")
test7_fig1b = plot_relative_difference(
    np.array(CI_test7_1b_auto.coverage), np.array(CI_test7_1b_max.coverage),
    plt_figure_num="CI test7 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_1b_auto.f.calculation_inputs()}")
test7_fig2  = plot_relative_difference(
    np.array(CI_test7_2_auto.coverage), np.array(CI_test7_2_max.coverage),
    plt_figure_num="CI test7 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_2_auto.f.calculation_inputs()}")
test7_fig2b = plot_relative_difference(
    np.array(CI_test7_2b_auto.coverage), np.array(CI_test7_2b_max.coverage),
    plt_figure_num="CI test7 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_2b_auto.f.calculation_inputs()}")
test7_fig3  = plot_relative_difference(
    np.array(CI_test7_3_auto.coverage), np.array(CI_test7_3_max.coverage),
    plt_figure_num="CI test7 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_3_auto.f.calculation_inputs()}")
test7_fig3b = plot_relative_difference(
    np.array(CI_test7_3b_auto.coverage), np.array(CI_test7_3b_max.coverage),
    plt_figure_num="CI test7 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_3b_auto.f.calculation_inputs()}")
test7_fig4  = plot_relative_difference(
    np.array(CI_test7_4_auto.coverage), np.array(CI_test7_4_max.coverage),
    plt_figure_num="CI test7 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_4_auto.f.calculation_inputs()}")
test7_fig4b = plot_relative_difference(
    np.array(CI_test7_4b_auto.coverage), np.array(CI_test7_4b_max.coverage),
    plt_figure_num="CI test7 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_4b_auto.f.calculation_inputs()}")
test7_fig5  = plot_relative_difference(
    np.array(CI_test7_5_auto.coverage), np.array(CI_test7_5_max.coverage),
    plt_figure_num="CI test7 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_5_auto.f.calculation_inputs()}")
test7_fig5b = plot_relative_difference(
    np.array(CI_test7_5b_auto.coverage), np.array(CI_test7_5b_max.coverage),
    plt_figure_num="CI test7 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_5b_auto.f.calculation_inputs()}")
test7_fig6  = plot_relative_difference(
    np.array(CI_test7_6_auto.coverage), np.array(CI_test7_6_max.coverage),
    plt_figure_num="CI test7 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_6_auto.f.calculation_inputs()}")
test7_fig6b = plot_relative_difference(
    np.array(CI_test7_6b_auto.coverage), np.array(CI_test7_6b_max.coverage),
    plt_figure_num="CI test7 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test7_6b_auto.f.calculation_inputs()}")


test8_fig1  = plot_relative_difference(
    np.array(CI_test8_1_auto.coverage), np.array(CI_test8_1_max.coverage),
    plt_figure_num="CI test8 1", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_1_auto.f.calculation_inputs()}")
test8_fig1b = plot_relative_difference(
    np.array(CI_test8_1b_auto.coverage), np.array(CI_test8_1b_max.coverage),
    plt_figure_num="CI test8 1b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_1b_auto.f.calculation_inputs()}")
test8_fig2  = plot_relative_difference(
    np.array(CI_test8_2_auto.coverage), np.array(CI_test8_2_max.coverage),
    plt_figure_num="CI test8 2", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_2_auto.f.calculation_inputs()}")
test8_fig2b = plot_relative_difference(
    np.array(CI_test8_2b_auto.coverage), np.array(CI_test8_2b_max.coverage),
    plt_figure_num="CI test8 2b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_2b_auto.f.calculation_inputs()}")
test8_fig3  = plot_relative_difference(
    np.array(CI_test8_3_auto.coverage), np.array(CI_test8_3_max.coverage),
    plt_figure_num="CI test8 3", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_3_auto.f.calculation_inputs()}")
test8_fig3b = plot_relative_difference(
    np.array(CI_test8_3b_auto.coverage), np.array(CI_test8_3b_max.coverage),
    plt_figure_num="CI test8 3b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_3b_auto.f.calculation_inputs()}")
test8_fig4  = plot_relative_difference(
    np.array(CI_test8_4_auto.coverage), np.array(CI_test8_4_max.coverage),
    plt_figure_num="CI test8 4", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_4_auto.f.calculation_inputs()}")
test8_fig4b = plot_relative_difference(
    np.array(CI_test8_4b_auto.coverage), np.array(CI_test8_4b_max.coverage),
    plt_figure_num="CI test8 4b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_4b_auto.f.calculation_inputs()}")
test8_fig5  = plot_relative_difference(
    np.array(CI_test8_5_auto.coverage), np.array(CI_test8_5_max.coverage),
    plt_figure_num="CI test8 5", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_5_auto.f.calculation_inputs()}")
test8_fig5b = plot_relative_difference(
    np.array(CI_test8_5b_auto.coverage), np.array(CI_test8_5b_max.coverage),
    plt_figure_num="CI test8 5b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_5b_auto.f.calculation_inputs()}")
test8_fig6  = plot_relative_difference(
    np.array(CI_test8_6_auto.coverage), np.array(CI_test8_6_max.coverage),
    plt_figure_num="CI test8 6", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_6_auto.f.calculation_inputs()}")
test8_fig6b = plot_relative_difference(
    np.array(CI_test8_6b_auto.coverage), np.array(CI_test8_6b_max.coverage),
    plt_figure_num="CI test8 6b", title="Diff between two {dim}d data[{shape}] - avg = {avg}, max = {max}\n"+f"{CI_test8_6b_auto.f.calculation_inputs()}")





test_fig1. savefig("testlib_diff/CI test 1.png")
test_fig1b.savefig("testlib_diff/CI test 1b.png")
test_fig2. savefig("testlib_diff/CI test 2.png")
test_fig2b.savefig("testlib_diff/CI test 2b.png")
test_fig3. savefig("testlib_diff/CI test 3.png")
test_fig3b.savefig("testlib_diff/CI test 3b.png")
test_fig4. savefig("testlib_diff/CI test 4.png")
test_fig4b.savefig("testlib_diff/CI test 4b.png")
test_fig5. savefig("testlib_diff/CI test 5.png")
test_fig5b.savefig("testlib_diff/CI test 5b.png")
test_fig6. savefig("testlib_diff/CI test 6.png")
test_fig6b.savefig("testlib_diff/CI test 6b.png")


test2_fig1. savefig("testlib_diff/CI test2 1.png")
test2_fig1b.savefig("testlib_diff/CI test2 1b.png")
test2_fig2. savefig("testlib_diff/CI test2 2.png")
test2_fig2b.savefig("testlib_diff/CI test2 2b.png")
test2_fig3. savefig("testlib_diff/CI test2 3.png")
test2_fig3b.savefig("testlib_diff/CI test2 3b.png")
test2_fig4. savefig("testlib_diff/CI test2 4.png")
test2_fig4b.savefig("testlib_diff/CI test2 4b.png")
test2_fig5. savefig("testlib_diff/CI test2 5.png")
test2_fig5b.savefig("testlib_diff/CI test2 5b.png")
test2_fig6. savefig("testlib_diff/CI test2 6.png")
test2_fig6b.savefig("testlib_diff/CI test2 6b.png")


test3_fig1. savefig("testlib_diff/CI test3 1.png")
test3_fig1b.savefig("testlib_diff/CI test3 1b.png")
test3_fig2. savefig("testlib_diff/CI test3 2.png")
test3_fig2b.savefig("testlib_diff/CI test3 2b.png")
test3_fig3. savefig("testlib_diff/CI test3 3.png")
test3_fig3b.savefig("testlib_diff/CI test3 3b.png")
test3_fig4. savefig("testlib_diff/CI test3 4.png")
test3_fig4b.savefig("testlib_diff/CI test3 4b.png")
test3_fig5. savefig("testlib_diff/CI test3 5.png")
test3_fig5b.savefig("testlib_diff/CI test3 5b.png")
test3_fig6. savefig("testlib_diff/CI test3 6.png")
test3_fig6b.savefig("testlib_diff/CI test3 6b.png")


test4_fig1. savefig("testlib_diff/CI test4 1.png")
test4_fig1b.savefig("testlib_diff/CI test4 1b.png")
test4_fig2. savefig("testlib_diff/CI test4 2.png")
test4_fig2b.savefig("testlib_diff/CI test4 2b.png")
test4_fig3. savefig("testlib_diff/CI test4 3.png")
test4_fig3b.savefig("testlib_diff/CI test4 3b.png")
test4_fig4. savefig("testlib_diff/CI test4 4.png")
test4_fig4b.savefig("testlib_diff/CI test4 4b.png")
test4_fig5. savefig("testlib_diff/CI test4 5.png")
test4_fig5b.savefig("testlib_diff/CI test4 5b.png")
test4_fig6. savefig("testlib_diff/CI test4 6.png")
test4_fig6b.savefig("testlib_diff/CI test4 6b.png")


test5_fig1. savefig("testlib_diff/CI test5 1.png")
test5_fig1b.savefig("testlib_diff/CI test5 1b.png")
test5_fig2. savefig("testlib_diff/CI test5 2.png")
test5_fig2b.savefig("testlib_diff/CI test5 2b.png")
test5_fig3. savefig("testlib_diff/CI test5 3.png")
test5_fig3b.savefig("testlib_diff/CI test5 3b.png")
test5_fig4. savefig("testlib_diff/CI test5 4.png")
test5_fig4b.savefig("testlib_diff/CI test5 4b.png")
test5_fig5. savefig("testlib_diff/CI test5 5.png")
test5_fig5b.savefig("testlib_diff/CI test5 5b.png")
test5_fig6. savefig("testlib_diff/CI test5 6.png")
test5_fig6b.savefig("testlib_diff/CI test5 6b.png")


test6_fig1. savefig("testlib_diff/CI test6 1.png")
test6_fig1b.savefig("testlib_diff/CI test6 1b.png")
test6_fig2. savefig("testlib_diff/CI test6 2.png")
test6_fig2b.savefig("testlib_diff/CI test6 2b.png")
test6_fig3. savefig("testlib_diff/CI test6 3.png")
test6_fig3b.savefig("testlib_diff/CI test6 3b.png")
test6_fig4. savefig("testlib_diff/CI test6 4.png")
test6_fig4b.savefig("testlib_diff/CI test6 4b.png")
test6_fig5. savefig("testlib_diff/CI test6 5.png")
test6_fig5b.savefig("testlib_diff/CI test6 5b.png")
test6_fig6. savefig("testlib_diff/CI test6 6.png")
test6_fig6b.savefig("testlib_diff/CI test6 6b.png")


test7_fig1. savefig("testlib_diff/CI test7 1.png")
test7_fig1b.savefig("testlib_diff/CI test7 1b.png")
test7_fig2. savefig("testlib_diff/CI test7 2.png")
test7_fig2b.savefig("testlib_diff/CI test7 2b.png")
test7_fig3. savefig("testlib_diff/CI test7 3.png")
test7_fig3b.savefig("testlib_diff/CI test7 3b.png")
test7_fig4. savefig("testlib_diff/CI test7 4.png")
test7_fig4b.savefig("testlib_diff/CI test7 4b.png")
test7_fig5. savefig("testlib_diff/CI test7 5.png")
test7_fig5b.savefig("testlib_diff/CI test7 5b.png")
test7_fig6. savefig("testlib_diff/CI test7 6.png")
test7_fig6b.savefig("testlib_diff/CI test7 6b.png")


test8_fig1. savefig("testlib_diff/CI test8 1.png")
test8_fig1b.savefig("testlib_diff/CI test8 1b.png")
test8_fig2. savefig("testlib_diff/CI test8 2.png")
test8_fig2b.savefig("testlib_diff/CI test8 2b.png")
test8_fig3. savefig("testlib_diff/CI test8 3.png")
test8_fig3b.savefig("testlib_diff/CI test8 3b.png")
test8_fig4. savefig("testlib_diff/CI test8 4.png")
test8_fig4b.savefig("testlib_diff/CI test8 4b.png")
test8_fig5. savefig("testlib_diff/CI test8 5.png")
test8_fig5b.savefig("testlib_diff/CI test8 5b.png")
test8_fig6. savefig("testlib_diff/CI test8 6.png")
test8_fig6b.savefig("testlib_diff/CI test8 6b.png")







input("Execution finished")
for i in range(100):
    input("")

