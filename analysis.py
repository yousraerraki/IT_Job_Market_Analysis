
import pandas as pd

df = pd.read_csv("data/ds_salaries.csv")

df = df.drop(columns=["Unnamed: 0"])
df = df.drop_duplicates()

print("Salaire moyen :")
print(df["salary_in_usd"].mean())
print(df["salary_in_usd"].max())
print(df["salary_in_usd"].min())
print(
    df.groupby("job_title")["salary_in_usd"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)
print(
    df.groupby("company_location")["salary_in_usd"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)
