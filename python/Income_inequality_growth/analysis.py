import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Baseline: Gini measured from 2010 to 2018
# Growth: average GDP per capita growth over the next five years(ie.2010 -->2011,2012,..,2015)

START_YEAR = 2010
END_YEAR = 2018
GROWTH_YEARS = 5

data_folder =Path(__file__).parent / "data"
gini=pd.read_csv(data_folder / "gini_data.csv")
growth=pd.read_csv(data_folder / "growth_data.csv")
gini=gini.rename(columns={'value':'gini'})
growth=growth.rename(columns={'value':'growth'})
gini["date"]=gini["date"].astype(int)
growth["date"]=growth["date"].astype(int)

print("Gini data:")
print(gini.head())
print("\nGrowth data:")
print(growth.head())
print("\nGini observations:",len(gini))
print("Growth observations:",len(growth))

gini_baseline = gini[
    gini["date"].between(START_YEAR, END_YEAR)
].copy()

print("\nBaseline Gini period:", START_YEAR, "to", END_YEAR)
print("Baseline Gini observations:", len(gini_baseline))
print("Countries in baseline sample:",
      gini_baseline["countryiso3code"].nunique())

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
gini_baseline["subsequent_growth"]= growth_values

print("\nBaseline dataset:")
print(gini_baseline.head(10))

print("\nObservations with subsequent growth:",
      gini_baseline["subsequent_growth"].notna().sum())

analysis_data = gini_baseline.dropna(subset=["subsequent_growth"]).copy()
print("\nFinal analysis dataset:")
print(analysis_data.head())
print("\nFinal analysis dataset observations:", len(analysis_data))
print("Countries in final analysis dataset:",
      analysis_data["countryiso3code"].nunique())

analysis_data.to_csv(data_folder / "analysis_data.csv", index=False)
print("\nFinal analysis dataset saved to 'analysis_data.csv'")

print("\nDescriptive statistics of the final analysis dataset:")
print(analysis_data[["subsequent_growth", "gini"]].describe())

plt.figure(figsize=(10, 6))
plt.scatter(analysis_data["gini"], analysis_data["subsequent_growth"], alpha=0.6)
plt.title("Income Inequality and Subsequent Economic Growth")
plt.xlabel("Gini Coefficient")
plt.ylabel("Average GDP per Capita Growth Over Following 5 Years")
plt.grid(True,alpha=0.3)
plt.show()

#Pearsons correlation coefficient between gini coefficient and subsequent growth

correlation=analysis_data["gini"].corr(analysis_data["subsequent_growth"])
print("\nCorrelation between Gini coefficient and subsequent growth:")
print(correlation)