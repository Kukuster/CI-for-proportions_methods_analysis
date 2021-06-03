# CI methods analyser
A toolkit for measuring efficacy of various methods for calculating confidence interval.
Currently provides with a toolking for measuring efficacy of methods for confidence interval for the following statistics:

 - proportion
 - difference between two proportions

An inspiraton for the library:
["Five Confidence Intervals for Proportions That You Should Know About" by Dr. Dennis Robert](https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f)


## NOTES

### !!!! Best practices publishing a package !!!!
https://realpython.com/pypi-publish-python-package/#preparing-your-package-for-publication


### Methods for measuring efficacy of CI methods
Two ways can be used to calculate efficacy of CI methods:
 - approximately, with random simulation (as implemented in R by Dr. Dennis Robert, see link above)
 - precisely, with the analytical solution

Both methods are implemented here for CI for both statistics: *proportion*, and *difference between two proportions*. For precise analytical solution a potentially lossy optimization was made. It's regulated with parameter `z_precision` which is by default calculated automatically and it has its drawbacks (see PLAN section).


## <u>Various links</u>
**1. Equivalence and Noninferiority Testing (as I understand, are fancy terms for 2-sided and 1-sided p tests for the difference between two proportions)**
 - **[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf) **
 - **[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Non-Inferiority_Tests_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Non-Inferiority_Tests_for_the_Difference_Between_Two_Proportions.pdf) **
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

