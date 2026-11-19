# Write a Python program to perform Exploratory Data Analysis (EDA) on a customer churn dataset and clean the data for further analysis.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("customer_churn.csv")
print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())
df.drop_duplicates(inplace=True)
df.fillna(df.select_dtypes(include="number").mean(), inplace=True)
df.fillna(df.select_dtypes(include="object").mode().iloc[0], inplace=True)

print("\nChurn Distribution:")
print(df["Churn"].value_counts())
sns.countplot(x="Churn", data=df)
plt.title("Customer Churn Distribution")
plt.show()

print("\nCorrelation Matrix:")
sns.heatmap(df.select_dtypes(include="number").corr(), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

print("\nCleaned Dataset:")
print(df.head())
df.to_csv("cleaned_customer_churn.csv", index=False)
print("\nCleaned data saved successfully.")
