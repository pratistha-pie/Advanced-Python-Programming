# Write a Python program to maintain sports equipment records using CSV file handling and command-line arguments.
import csv
import sys
filename = sys.argv[1]
with open(filename, "r") as file:
    equipment = list(csv.DictReader(file))
print("All Equipment Records:")
for item in equipment:
    print(item)

eid = input("Enter Equipment ID to search: ")
found = False
for item in equipment:
    if item["Equipment ID"] == eid:
        print("Equipment Found:")
        print(item)
        found = True
        break
if not found:
    print("Equipment not found.")
