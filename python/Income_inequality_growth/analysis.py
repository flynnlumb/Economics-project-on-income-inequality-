import pandas as pd
import requests 
from pathlib import Path
url = "https://api.worldbank.org/v2/country/all/indicator/SI.POV.GINI?format=json&per_page=20000"
response = requests.get(url)
data =response.json()[1]
df = pd.DataFrame(data)
df = df[['countryiso3code', 'country', 'date', 'value']]
df["country"] = df["country"].apply(lambda x: x['value'])
df =df.dropna(subset=['value'])
print(df.head())
print(df.shape)
print(df['country'].nunique())
print(df['date'].min(), df['date'].max())

data_folder =Path(__file__).parent / "data"
data_folder.mkdir(exist_ok=True)
df.to_csv(data_folder / "gini_data.csv", index=False)