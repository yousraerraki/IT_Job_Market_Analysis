import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/ds_salaries.csv")


df = df.drop(columns=["Unnamed: 0"])
df = df.drop_duplicates()


country_jobs = df["company_location"].value_counts().head(10)

print(country_jobs)


plt.figure(figsize=(10,6))

country_jobs.plot(kind="bar")

plt.title("Top 10 Countries by Number of Data Jobs")
plt.xlabel("Country")
plt.ylabel("Number of Jobs")

plt.xticks(rotation=45)

plt.tight_layout()

plt.show()