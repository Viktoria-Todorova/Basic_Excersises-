steps_count = 0
while steps_count <= 10000:
    steps = input()

    if steps != "Going home":
        steps_count += int(steps)
    else:
        steps_count += int(input())
        break

if steps_count >= 10000:
    print("Goal reached! Good job!")
    print(f"{steps_count - 10000} steps over the goal!")
elif steps_count < 10000:
    print(f"{10000 - steps_count} more steps to reach goal.")






