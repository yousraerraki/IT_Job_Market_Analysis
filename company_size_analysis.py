import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/ds_salaries.csv")

df = df.drop(columns=["Unnamed: 0"])
df = df.drop_duplicates()

company_salary = df.groupby("company_size")["salary_in_usd"].mean()

print(company_salary)

plt.figure(figsize=(6,5))

company_salary.plot(kind="bar")

plt.title("Average Salary by Company Size")
plt.xlabel("Company Size")
plt.ylabel("Average Salary (USD)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()