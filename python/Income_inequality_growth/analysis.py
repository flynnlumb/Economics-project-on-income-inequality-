import pandas as pd
from pathlib import Path
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
