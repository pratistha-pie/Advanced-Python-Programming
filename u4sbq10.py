# Write a Python program to analyze hotel room rents using NumPy and Pandas.
import numpy as np
import pandas as pd
rents = np.array([2000, 3500, 4500, 5000, 3000, 6000])
rooms = ["Standard", "Deluxe", "Suite", "Luxury", "Single", "Presidential"]
print("Mean Rent:", np.mean(rents))
print("Median Rent:", np.median(rents))
print("Maximum Rent:", np.max(rents))
print("Minimum Rent:", np.min(rents))

df = pd.DataFrame({
    "Room Type": rooms,
    "Room Rent": rents})
print("\nHotel Room Records:")
print(df)
print("\nRooms with rent above ₹4000:")
print(df[df["Room Rent"] > 4000])
