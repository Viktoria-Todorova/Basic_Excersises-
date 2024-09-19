name_actor = input()
points_from_academy = float(input())
num_people = int(input())
is_enough = False

for people in range(num_people):
    name_person = input()
    points_given = float(input())

    points_from_academy += ((len(name_person) * points_given)/2)

    if points_from_academy >= 1250.5:
        print(f"Congratulations, {name_actor} got a nominee for leading role with {points_from_academy:.1f}!")
        is_enough = True
        break

if not is_enough:
    print(f"Sorry, {name_actor} you need {(1250.5-points_from_academy):.1f} more!")