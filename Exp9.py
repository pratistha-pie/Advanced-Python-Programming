# Write a Python program to read data from a CSV file, convert it into JSON format, and write it to a JSON output file.
import csv
import json
with open("input.csv", "r") as file:
    data = list(csv.DictReader(file))

with open("output.json", "w") as file:
    json.dump(data, file, indent=4)
print("CSV data successfully converted to JSON format.")