import pandas as pd
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



