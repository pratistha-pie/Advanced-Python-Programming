# Write a Python program to maintain hospital patient records using CSV file handling.
import csv
with open("patients.csv", "r") as file:
    patients = list(csv.DictReader(file))
print("All Patient Records:")
for patient in patients:
    print(patient)

pid = input("Enter Patient ID to search: ")
found = False
for patient in patients:
    if patient["Patient ID"] == pid:
        print("Patient Found:")
        print(patient)
        found = True
        break
if not found:
    print("Patient not found.")
