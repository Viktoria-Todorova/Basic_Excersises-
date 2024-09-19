number_students = int(input())
count_student_1 = count_student_2 = count_student_3 = count_student_4 = 0
total_sum = 0
for every_student in range(number_students):
    grade = float(input())

    if 2.00 <= grade < 3.00:
        count_student_1 += 1
        total_sum += grade
    elif 3 <= grade < 4.00:
        count_student_2 += 1
        total_sum += grade
    elif 4.00 <= grade < 5.00:
        count_student_3 += 1
        total_sum += grade
    elif grade >= 5.00:
        count_student_4 += 1
        total_sum += grade

average_grade = total_sum / number_students
print(f"Top students: {(count_student_4/number_students*100):.2f}%")
print(f"Between 4.00 and 4.99: {(count_student_3/number_students*100):.2f}%")
print(f"Between 3.00 and 3.99: {(count_student_2/number_students*100):.2f}%")
print(f"Fail: {(count_student_1/number_students*100):.2f}%")
print(f"Average:{average_grade: .2f}")
