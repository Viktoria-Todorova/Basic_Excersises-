k= int(input())
l= int(input())
m= int(input())
n=int(input())
digit1 = digit2=0
digit3 = digit4 = 0
flag = False
change = 0
for firs_number_first in range (k ,9):
    if firs_number_first %2 == 0:
        for second_number_first in range(9, l-1, -1):
            if second_number_first %2 != 0:
                for firs_number_second in range (m , 9):
                    if firs_number_second %2 == 0:
                        for second_number_second in range (9, n -1, -1):
                            if second_number_second %2 != 0:
                                num1 = f"{firs_number_first}{second_number_first}"
                                num2 = f"{firs_number_second}{second_number_second}"

                                if num1 == num2:
                                    if change < 6:
                                        print("Cannot change the same player.")
                                        flag = False
                                    else:
                                        break

                                elif num1 != num2:
                                    change += 1
                                    if change <= 6:
                                        flag = True
                                        print(f"{num1} - {num2}")
                                    else:
                                        break













