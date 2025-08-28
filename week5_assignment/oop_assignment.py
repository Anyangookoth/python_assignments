# Step 1: Define a base class Person
# This class will be inherited by both Doctor and Patient
class Person:
    def __init__(self, name, age):
        self._name = name  # Protected attribute
        self._age = age

    def get_name(self):
        return self._name

# Step 2: Define the Patient class that inherits from Person
class Patient(Person):
    def __init__(self, name, age, patient_id, diagnosis):
        super().__init__(name, age)
        self._patient_id = patient_id
        self._diagnosis = diagnosis

    def get_details(self):
        return f"Patient ID: {self._patient_id}, Name: {self._name}, Age: {self._age}, Diagnosis: {self._diagnosis}"

# Step 3: Define the Doctor class that inherits from Person
class Doctor(Person):
    def __init__(self, name, age, specialty):
        super().__init__(name, age)
        self._specialty = specialty

    def get_details(self):
        return f"Dr. {self._name}, Age: {self._age}, Specialty: {self._specialty}"

# Step 4: Define the Hospital class to manage patients and doctors
class Hospital:
    def __init__(self, name):
        self._name = name
        self._patients = []
        self._doctors = []

    def add_patient(self, patient):
        if isinstance(patient, Patient):
            self._patients.append(patient)

    def add_doctor(self, doctor):
        if isinstance(doctor, Doctor):
            self._doctors.append(doctor)

    def list_patients(self):
        print(f"\n🧑‍⚕️ Patients at {self._name}:")
        for patient in self._patients:
            print(patient.get_details())

    def list_doctors(self):
        print(f"\n👨‍⚕️ Doctors at {self._name}:")
        for doctor in self._doctors:
            print(doctor.get_details())

# Step 5: Create a main function to test the classes
def main():
    print("✅ Starting test...")

    # Create a Person object
    person = Person("Winnie", 32)
    print("Person name is:", person.get_name())

    # Create a Patient object
    patient = Patient("Amina", 28, "P001", "Malaria")
    print(patient.get_details())

    # Create a Doctor object
    doctor = Doctor("Otieno", 45, "Internal Medicine")
    print(doctor.get_details())

    # Create a Hospital object
    hospital = Hospital("Nairobi General")

    # Add patient and doctor to the hospital
    hospital.add_patient(patient)
    hospital.add_doctor(doctor)

    # List all patients and doctors
    hospital.list_patients()
    hospital.list_doctors()

# Step 6: Run the main function when the file is executed
if __name__ == "__main__":
    main()

    # Base class
class Vehicle:
    def move(self):
        print("Vehicle is moving")

# Derived classes with polymorphic behavior
class Car(Vehicle):
    def move(self):
        print("Driving")

class Plane(Vehicle):
    def move(self):
        print("Flying")

class Boat(Vehicle):
    def move(self):
        print("Sailing")

# Function to test polymorphism
def test_polymorphism():
    print("\nPolymorphism Test:")
    vehicles = [Car(), Plane(), Boat()]
    for vehicle in vehicles:
        vehicle.move()

# Run the test
test_polymorphism()