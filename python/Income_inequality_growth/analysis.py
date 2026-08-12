import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
from pathlib import Path


# Data folder

data_folder = Path(__file__).parent / "data"


# Load datasets

gini = pd.read_csv(data_folder / "gini_data.csv")
growth = pd.read_csv(data_folder / "growth_data.csv")
gdp = pd.read_csv(data_folder / "gdp_per_capita_data.csv")


# Rename variables

gini = gini.rename(columns={"value": "gini"})
growth = growth.rename(columns={"value": "growth"})


# Convert dates to integers

gini["date"] = gini["date"].astype(int)
growth["date"] = growth["date"].astype(int)
gdp["date"] = gdp["date"].astype(int)


# Baseline specification

START_YEAR = 2010
END_YEAR = 2018
GROWTH_YEARS = 5


# Select baseline Gini observations

gini_baseline = gini[
    gini["date"].between(START_YEAR, END_YEAR)
].copy()

print("\nBaseline Gini period:", START_YEAR, "to", END_YEAR)
print("Baseline Gini observations:", len(gini_baseline))
print(
    "Countries in baseline sample:",
    gini_baseline["countryiso3code"].nunique()
)


# Calculate subsequent five-year average growth

growth_values = []

for _, row in gini_baseline.iterrows():

    country = row["countryiso3code"]
    gini_year = row["date"]

    following_growth = growth[
        (growth["countryiso3code"] == country) &
        (growth["date"] > gini_year) &
        (growth["date"] <= gini_year + GROWTH_YEARS)
    ]

    if len(following_growth) == GROWTH_YEARS:
        average_growth = following_growth["growth"].mean()
    else:
        average_growth = None

    growth_values.append(average_growth)


gini_baseline["subsequent_growth"] = growth_values


# Remove observations without five years of subsequent growth

analysis_data = gini_baseline.dropna(
    subset=["subsequent_growth"]
).copy()


print("\nFinal analysis dataset:")
print(analysis_data.head())

print(
    "\nFinal analysis dataset observations:",
    len(analysis_data)
)

print(
    "Countries in final analysis dataset:",
    analysis_data["countryiso3code"].nunique()
)


# Merge GDP per capita

analysis_data = analysis_data.merge(
    gdp[
        ["countryiso3code", "date", "gdp_per_capita"]
    ],
    on=["countryiso3code", "date"],
    how="left"
)


print("\nAnalysis dataset with GDP per capita:")
print(analysis_data.head())

print(
    "\nObservations with GDP per capita:",
    analysis_data["gdp_per_capita"].notna().sum()
)

print(
    "Observations without GDP per capita:",
    analysis_data["gdp_per_capita"].isna().sum()
)


# Save analysis dataset

analysis_data.to_csv(
    data_folder / "analysis_data.csv",
    index=False
)

print("\nAnalysis dataset saved.")


# Descriptive statistics

print("\nDescriptive statistics:")

print(
    analysis_data[
        ["subsequent_growth", "gini", "gdp_per_capita"]
    ].describe()
)


# Scatter plot

plt.figure(figsize=(10, 6))

plt.scatter(
    analysis_data["gini"],
    analysis_data["subsequent_growth"],
    alpha=0.6
)

plt.title(
    "Income Inequality and Subsequent Economic Growth"
)

plt.xlabel("Gini Coefficient")

plt.ylabel(
    "Average GDP per Capita Growth Over Following 5 Years"
)

plt.grid(True, alpha=0.3)

plt.show()


# Pearson correlation

correlation = analysis_data[
    "gini"
].corr(
    analysis_data["subsequent_growth"]
)

print(
    "\nCorrelation between Gini coefficient and subsequent growth:"
)

print(correlation)


# Baseline OLS regression

X = analysis_data["gini"]
y = analysis_data["subsequent_growth"]

X = sm.add_constant(X)

model = sm.OLS(y, X).fit()


print("\nBaseline OLS Regression Results:")

print("\nCoefficients:")
print(model.params)

print("\nP-values:")
print(model.pvalues)

print("\nR-squared:")
print(model.rsquared)

print("\nConfidence intervals:")
print(model.conf_int())

#Controlled OLS regression
#Controls for GDP per capita in the year of the Gini observation

X=analysis_data[["gini", "gdp_per_capita"]]
X = sm.add_constant(X)

y=analysis_data["subsequent_growth"]

controlled_model = sm.OLS(y, X).fit()

print("\nControlled OLS Regression Results:")
print("\nCoefficients:")
print(controlled_model.params)
print("\nP-values:")
print(controlled_model.pvalues)
print("\nR-squared:")
print(controlled_model.rsquared)
print("\nConfidence intervals:")
print(controlled_model.conf_int())
