n = int(input())

left_sum = 0
right_sum = 0

# Четем първите n числа и ги добавяме към left_sum
for i in range(n):
    number = int(input())
    left_sum += number

# Четем следващите n числа и ги добавяме към right_sum
for i in range(n):
    number = int(input())
    right_sum += number

# Проверяваме дали лявата и дясната сума са равни
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")