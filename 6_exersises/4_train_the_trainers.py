people_in_jury = int(input())
count_presentations = total_score = 0

while True:
    name_presentation = input()
    if name_presentation == "Finish":
        break

    score_per_presentatio = 0.0
    count_presentations +=1

    for grade in range(people_in_jury):
        score = float(input())
        score_per_presentatio += score

    avg_score = score_per_presentatio/ people_in_jury
    total_score += avg_score
    print(f"{name_presentation} - {avg_score:.2f}.")

print(f"Student's final assessment is {(total_score/count_presentations):.2f}.")
