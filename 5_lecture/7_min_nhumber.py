from sys import maxsize
min_num = maxsize

while True:
    number = input()

    if number == "Stop":
        break

    current_num =int(number)

    if current_num < min_num:
        min_num = current_num

print(min_num)