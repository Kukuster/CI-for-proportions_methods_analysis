# CI for proportions methods analysis
Calculating efficacy with simulation of various methods for calculating confidence interval for proportions

sources:
[https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f](https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f)


## PLAN (2021.03.29)

### Plottting

To figure out the best method for calculating _**CI for the difference between two proportions**_, I have to make one more simulation and plot it as a 2d-histogram:

https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.hist2d.html

The idea is that I would have a `dark_background` style, with a gradient colors. e.g. for a 95%CI:
 - 95% coverage - white color,
 - 50% coverage - red color,
 - 100% - green or blue


### Simulating methods

Start with this document:

**[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf) **

Figure out how exaclty to implement the methods and evaluate their efficacy.

E.g. as I understood  the **Farrington and Manning’s Score** method, the main idea is to calculate 2 values for delta0, that is the confidence interval for the delta (which equals to p1_hat - p2_hat)

For this, we calculate everything and get zFMD = F(delta0), where F is some sick humongous function over the unknown variable - delta0. It involves polynomials of delta0 up to 4th power, cosines and arccosines of that, and a square root over all that. Then the the delta0 is calculated as a solution for zFMD = F(delta0) for zFMD equals +-z-score for the given alpha. It's very likely that it is impossible to solve this analytically (hence such a recipe). Therefore, I have to figure out a way to implement numerical methods for solving this in general form.

By the way, I think "MLE" there means "Maximum Likelihood Estimate", but I'm not sure.

## Links
**1. Equivalence and Noninferiority Testing (as I understand, are fancy terms for 2-sided and 1-sided p tests for the difference between two proportions)**
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
**4. A concern of the vaccine causing Bell's palsy**
 - [https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7874945/](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7874945/) or [https://www.sciencedirect.com/science/article/pii/S266635462100020X?via%3Dihub](https://www.sciencedirect.com/science/article/pii/S266635462100020X?via%3Dihub) 