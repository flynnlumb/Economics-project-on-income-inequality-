# Economics-project-on-income-inequality-
An empirical investigation into the relationship between income inequality and economic growth using statistical analysis tools in Python

1.Research Question:
To what extent does income inequality in a nation affect subsequent economic growth?
-This project will investigate the relationship between the distribution of income in a country and its rate of economic growth in the years that follow. Using cross-country data, this analysis will examine whether higher levels of inequality affect future growth, before adding other economic variables that may influence growth to assess if the relationship persists. 

2.Hypothesis:

Higher levels of income inequality are associated with lower subsequent economic growth:
 
This hypothesis is based on the possibility that greater income inequality may lead to worse access to education, healthcare and financial oppurtunities for lower-income consumers which as a result could reduce human capital accumulation and productive investment.

However, this is not the only theoretical prediction and so the analysis will consider whether the evidence points towards a positive or conditional relationship instead. 

3.Data:

This project uses data from the World Bank.
The main variables are: 
-GINI Index, which measures the distribution of income in society, with 0 being perfect equality and 100 being perfect inequality, used as my measure of income inequality
-Real GDP/capita growth, which I'm using to measure subsequent economic growth

The analysis uses GINI observations from 2010-2018 inclusive, with subsequent growth being measured as the average rate of real gdp/capita growth in the following five years.
The final baseline dataset contains 754 country-year observations across 156 countries. 
Any observation without a five year growth period were excluded from the data.

4.Methodology

I initially established a baseline specification using Gini observations from 2010-18. For each of these I measured subsequent economic growth as the average of the next five years year on year real gdp per capita. Observations without a complete five year period were excluded which produced a final baseline dataset of 754 entries across 156 countries.
I then calculated the pearsons correlation coefficient for the data and plotted it on a scatter graph finding the correlation coefficient to be -0.0474. 
Next I calculated a baseling OLS regression model for the data where Subsequent Growth = β₀ + β₁Gini + ε
I then calculated a controlled OLS regression using GDP/capita at the time the Gini coefficient was measured as a control where: β₀ + β₁Gini + β₂GDP per capita + ε , which allowed me to examine whether the relationship between inequality and subsequent growth changes when accounting for initial income levels.