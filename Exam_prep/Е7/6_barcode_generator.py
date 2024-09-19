num1 = input()
num2 = input()
flag = False
current_digit1 = current_digit2 = current_digit3 = current_digit4 =0
for digit1 in range (int(num1[0]), int(num2[0]) + 1):
    if digit1 % 2 == 0:
        continue

    for digit2 in range (int(num1[1]), int(num2[1]) + 1):
        if digit2 % 2 == 0:
            continue

        for digit3 in range(int(num1[2]), int(num2[2]) + 1):
            if digit3 % 2 == 0:
                continue

            for digit4 in range(int(num1[3]), int(num2[3]) + 1):
                if digit4 % 2 == 0:
                    continue

                print(f"{digit1}{digit2}{digit3}{digit4}", end = " " )








