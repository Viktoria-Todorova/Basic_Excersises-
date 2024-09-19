number = int(input())
is_found = False
for num in range(1111, 10000):
    number_to_string = str(num)

    for digit in number_to_string:
        if int(digit) == 0:
            is_found = False
            break
        elif number % int(digit) == 0:
            is_found = True
        else:
            is_found = False
            break


    if is_found:
        print(num, end = " ")
