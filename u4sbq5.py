# Write a Python program to analyze electricity bills using NumPy and Pandas.
import numpy as np
import pandas as pd
bills = np.array([1500, 2500, 3500, 4000, 2000, 4500])
consumers = ["Amit", "Rahul", "Priya", "Neha", "Riya", "Karan"]
print("Mean Bill:", np.mean(bills))
print("Median Bill:", np.median(bills))
print("Maximum Bill:", np.max(bills))
print("Minimum Bill:", np.min(bills))

df = pd.DataFrame({
    "Consumer": consumers,
    "Bill Amount": bills})
print("\nElectricity Bill Records:")
print(df)
print("\nConsumers with bills above ₹3000:")
print(df[df["Bill Amount"] > 3000])
