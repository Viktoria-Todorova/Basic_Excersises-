from sys import maxsize
max_num = -maxsize


while True:
    number = input()

    if number == "Stop":
        break

    current_num =int(number)

    if current_num > max_num:
        max_num = current_num

print(max_num)