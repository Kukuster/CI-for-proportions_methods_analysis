# CI methods efficacy analysis toolkit
Measures efficacy of methods for calculating confidence interval.
Currently provides with a toolking for measuring efficacy of methods for confidence interval for the following statistics:

 - proportion
 - difference between two proportions

An inspiraton for the library:
[https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f](https://towardsdatascience.com/five-confidence-intervals-for-proportions-that-you-should-know-about-7ff5484c024f)


## PLAN (TODOs)

### **_V_ 1. Refactor main function**
Both implementations of calculating coverage (`calculate_coverage_randomly` and `calculate_coverage_analytically`) in both toolkits (`CI_method_for_proportion_efficacy` and `CI_method_for_diff_betw_two_proportions_efficacy`) have way too much in common. Gonna DRY out a lot of code. Won't be easy though.

### **_V_ 2. Improve `proportions` interface**
Proportions are passed to these functions in a wierd way.
Let proportions be passed to functions as either `List[str]`, `List[float]` or `Tuple[str,str,str]`

### **_V_ 3. Improve automatic precision of analytical solution**
`z_precision` should slightly increase with increasing `confidence`. It's been shown that simply making `z_precision` to correspond to `p_precision` that equals to a number 1000 times closer to 1 than `confidence` doesn't quite nail it. It does for lower `confidence`, but with confidence 99.99% and more, `z_precision` maybe should increase even more. It turns out, for `confidence = 99.99%` having `z_precision = 99.999_99%` is good, but for `99.999_943%` having `z_precision = 99.999_999_943%` isn't enough.

### **4. Tidy up & publish**
 - remove all imports of whole libraries, leave only imports of necessary parts (i guess this is the right way to do it)
 - prepare structure to publish as a package
 - publish as `pip` package

### **Also:**
see `BACKLOG.md`



## NOTES

### Methods for measuring efficacy of CI methods
Two ways can be used to calculate efficacy of CI methods:
 - approximately, with random simulation (as implemented in R by Dr. Dennis Robert, see link above)
 - precisely, with the analytical solution

Both methods are implemented here for CI for both statistics: *proportion*, and *difference between two proportions*. For precise analyticsl solution a potentially lossy optimization has been made. It's regulated with parameter `z_precision` which is by default calculated automatically and it has its drawbacks (see PLAN section).


### Figuring out how to use certain advanced methods for calculating CI for the *difference between two proportions*

Start with this document:

**[https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf](https://ncss-wpengine.netdna-ssl.com/wp-content/themes/ncss/pdf/Procedures/PASS/Confidence_Intervals_for_the_Difference_Between_Two_Proportions.pdf) **

Figure out how exaclty to implement the methods and evaluate their efficacy.

E.g. as I understood  the **Farrington and Manning’s Score** method, the main idea is to calculate 2 values for delta0, that is the confidence interval for the delta (which equals to p1_hat - p2_hat)

For this, we calculate everything and get zFMD = F(delta0), where F is some sick humongous function over the unknown variable - delta0. It involves polynomials of delta0 up to 4th power, cosines and arccosines of that, and a square root over all that. Then the the delta0 is calculated as a solution for zFMD = F(delta0) for zFMD equals +-z-score for the given alpha. It's very likely that it is impossible to solve this analytically (hence such a recipe). Therefore, I have to figure out a way to implement numerical methods for solving this in general form.

By the way, I think "MLE" there means "Maximum Likelihood Estimate", but I'm not sure.

## <u>Links</u>
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

