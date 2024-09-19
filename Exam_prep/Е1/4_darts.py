name = input()
start_points = 301
count_shots = 0
count_points = count_fails = 0
while True:
    place = input()

    if place == "Retire":
        print(f"{name} retired after {count_fails} unsuccessful shots.")
        break

    points = int(input())

    if place == "Single":
        count_points = points
    elif place == "Double":
        count_points = points * 2
    elif place == "Triple":
        count_points = points * 3

    if count_points <= start_points:
        count_shots +=1
        start_points -= count_points
    else:
        count_fails += 1
        continue

    if start_points == 0:
        print(f"{name} won the leg with {count_shots} shots.")
        break





