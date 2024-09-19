name = input()
grades = 0
years = 0
failed = 0

while years < 12:
    annual_grade = float(input())

    if annual_grade < 4:
        failed += 1
        if failed == 2:
            print(f"{name} has been excluded at {years + 1} grade")
            break
        continue

    years += 1
    grades += annual_grade
else:
    average_grade = grades / 12
    print(f"{name} graduated. Average grade: {average_grade:.2f}")

