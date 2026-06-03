import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("employees.csv")

print("Original Data")
print(df)

# Remove duplicate rows
df = df.drop_duplicates()

# Fill missing values
df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Salary"] = df["Salary"].fillna(df["Salary"].mean())

print("\nCleaned Data")
print(df)

plt.bar(df["Name"], df["Salary"])

plt.title("Employee Salary Analysis")
plt.xlabel("Employee")
plt.ylabel("Salary")

plt.savefig("output.png")
plt.show()