period = int(input())
treated_patients = 0
untreated_patients = 0
number_doctors = 7
for time in range(1,period +1):
    number_patients = int(input())

    if time % 3 == 0:
        if untreated_patients > treated_patients:
            number_doctors += 1

    if number_patients <= number_doctors:
        treated_patients += number_patients
    elif number_patients > number_doctors:
        treated_patients += number_doctors
        untreated_patients += number_patients - number_doctors

print(f"Treated patients: {treated_patients}.")
print(f"Untreated patients: {untreated_patients}.")




