import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/ds_salaries.csv")


df = df.drop(columns=["Unnamed: 0"])
df = df.drop_duplicates()


experience_salary = df.groupby("experience_level")["salary_in_usd"].mean()

print(experience_salary)


plt.figure(figsize=(8,5))

experience_salary.plot(kind="bar")

plt.title("Average Salary by Experience Level")
plt.xlabel("Experience Level")
plt.ylabel("Average Salary (USD)")

plt.xticks(rotation=0)

plt.tight_layout()

plt.show()