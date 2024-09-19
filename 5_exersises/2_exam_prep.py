failed_score = int(input())
last_name = ""
low_grade = av_grade = num_problems = average_grade = 0
while True:
    question_name = input()

    if question_name != "Enough":
        score = int(input())
        if score <= 4:
            low_grade += 1
            av_grade += score
            num_problems += 1
            last_name = question_name
        elif 4 < score <= 6:
            av_grade += score
            num_problems += 1
            last_name = question_name
    elif question_name == "Enough":
        average_grade = av_grade / num_problems
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {num_problems}")
        print(f"Last problem: {last_name}")
        break

    if low_grade >= failed_score:
        print(f"You need a break, {failed_score} poor grades.")
        break



