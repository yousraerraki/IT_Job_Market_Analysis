import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("data/ds_salaries.csv")


df = df.drop("Unnamed: 0", axis=1)
df = df.drop_duplicates()


top_jobs = df["job_title"].value_counts().head(10)


plt.figure(figsize=(10,6))
top_jobs.plot(kind="bar")

plt.title("Top 10 Data Jobs")
plt.xlabel("Job Title")
plt.ylabel("Number of Jobs")

plt.xticks(rotation=45, ha="right")

plt.tight_layout()

plt.show()