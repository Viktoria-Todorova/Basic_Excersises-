steps_in_game = int(input())
total_sum = 0
count_1 = count_2 = count_3 = count_4 = count_5 = count_6 = 0
for step in range(0,steps_in_game):
    current_step = int(input())

    if 0 <= current_step <= 9:
        total_sum += current_step * 0.2
        count_1 += 1
    elif 10 <= current_step <= 19:
        total_sum += current_step * 0.3
        count_2 += 1
    elif 20 <= current_step <= 29:
        total_sum += current_step * 0.4
        count_3 += 1
    elif 30 <= current_step <= 39:
        total_sum += 50
        count_4 += 1
    elif 40 <= current_step <= 50:
        total_sum += 100
        count_5 += 1
    else:
        total_sum /= 2
        count_6 += 1

print(f"{total_sum:.2f}")
print(f"From 0 to 9: {(count_1/steps_in_game*100):.2f}%")
print(f"From 10 to 19: {(count_2/steps_in_game*100):.2f}%")
print(f"From 20 to 29: {(count_3/steps_in_game*100):.2f}%")
print(f"From 30 to 39: {(count_4/steps_in_game*100):.2f}%")
print(f"From 40 to 50: {(count_5/steps_in_game*100):.2f}%")
print(f"Invalid numbers: {(count_6/steps_in_game*100):.2f}%")
