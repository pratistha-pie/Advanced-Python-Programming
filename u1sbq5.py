# Hospital Patient Management System
class Patient:
    def __init__(self, patient_id, name, treatment_cost):
        self.patient_id = patient_id
        self.name = name
        self.treatment_cost = treatment_cost

    def category(self):
        if self.treatment_cost >= 10000:
            return "Special"
        else:
            return "General"

    def display(self):
        print("Patient ID:", self.patient_id)
        print("Name:", self.name)
        print("Treatment Cost: Rs.", self.treatment_cost)
        print("Category:", self.category())
        print("------------------------")

class Hospital:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient):
        self.patients.append(patient)

    def display_all(self):
        print("\n--- All Patient Records ---")
        for patient in self.patients:
            patient.display()

hospital = Hospital()

n = int(input("Enter number of patients: "))

for i in range(n):
    print("\nEnter Patient", i + 1, "Details")

    patient_id = int(input("Enter Patient ID: "))
    name = input("Enter Patient Name: ")
    cost = float(input("Enter Treatment Cost: "))

    patient = Patient(patient_id, name, cost)
    hospital.add_patient(patient)

hospital.display_all()
