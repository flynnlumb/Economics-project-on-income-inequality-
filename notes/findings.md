Findings:

1.Initial visual analysis of scatter graph of Gini vs Subsequent growth rate
 Most observations cluster in the Gini coefficient range of about 25-45 with far fewer data points at the extremes.Upon first look there is no obvious linear relationship between Gini and subsequent growth rate.Growth rates between 0% and 4% occur across much of the inequality range, while growth outcomes vary significantly at most Gini levels.There appears to be some evidence of more negative growth among the highest inequality observations, however these are relativelty sparse. Also, the highest growth levels tend to occur at moderate Gini levels. Overall the visual evidence suggests that inequality alone does not strongly determine subsequent growth, although the relationship does need statistical testing.

2.Pearsons correlation coefficient
 Found to be -0.0474 to 3 significant figures which shows a weak negative correlation between the gini coefficient and subsequent growth, however is nowhere near strong enough to meaningfully conclude that inequality reduces growth.

3.Ordinary least squares regression analysis:
 Results obtained: Baseline OLS Regression Results:

Coefficients:
const    2.428519
gini    -0.012389
dtype: float64

P-values:
const    9.327496e-12
gini     1.933631e-01
dtype: float64

R-squared:
0.0022487057272289057

Confidence intervals:
              0         1
const  1.740128  3.116911
gini  -0.031071  0.006293

The regression finds no significant relationship between income inequality (Gini) and subsequent 5-year GDP growth (β = -0.012, p = 0.19). The 95% CI for the Gini coefficient spans zero (-0.031 to 0.006), so we can't rule out no effect at all. R²=0.00225 means Gini explains essentially none of the variance in growth. Overall this simple bivariate model shows no evidence that inequality predicts subsequent growth in this dataset.

4.OLS Regression controlled for GDP/capita at time of Gini measurement: 
Controlled OLS Regression Results:

Coefficients:
const             3.765998
gini             -0.037468
gdp_per_capita   -0.000021
dtype: float64

P-values:
const             1.693724e-20
gini              1.830143e-04
gdp_per_capita    2.915967e-11
dtype: float64

R-squared:
0.059354025719212555

Confidence intervals:
                       0         1
const           2.992327  4.539670
gini           -0.057029 -0.017906
gdp_per_capita -0.000028 -0.000015

After controlling for GDP per capita the estimated relationship between income inequality and subsequent 5 year average growth rate became negative and statistically significant(β=-0.0375 to 3sf and p<0.001). The 95% confidence interval ranges from -0.0570 to -0.0179, so the interval is negative for the estimated coefficient. The R² value increased to 0.0594 which indicates the controlled model explains more variance in the subsequent growth than the baseline, however it is still low at 5.94% and it remains an observational relationship and should not be interpreted as casual.

5.Testing robustness of controlled regression
-I found the correlation between Gini coefficient and GPP/capita in the same year to be
0.373 which shows that in my sample, countries with a higher Gini coefficient tend to have a lower GDP per capita. However this is only a moderate negative correlation and so does not suggest a severe multicollinearity by itself.

-I then ran a VIF test on the same two variables and got the value to be 1.53 which is a relatively low value and so suggests there is a low multicollinearity between the two variables. Therefore multicollineararity does not appear to be a major concern in the controlled regression.

-Next I performed an influential observation robustness check.To do this, I excluded observations with cook's distance above the 4/n threshold and with this data set produced a controlled regression with a Gini coefficient of β = −0.0353 (p < 0.001), compared with −0.0375 (p < 0.001) in the full controlled model. The 95% confidence interval remains entirely negative which suggests that the negative relationship between inequality and subsequent growth is not driven solely by observations identified as possibly influential.R² increased from 0.0594 to 0.1467 in the restricted sample.