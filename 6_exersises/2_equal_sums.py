num1 = int(input())
num2 = int(input())


for num in range(num1, num2 + 1):
    sum_even = sum_odd = 0 #zanulyavame gi zashtoto se sumirat, na anas ni triabbva za vsiako edno chislo
    for idx, digit in enumerate(str(num)):
        if idx % 2 == 0:
            sum_even += int(digit) #zashoto ni e zapazeno kato str i go obrushtame v int
        elif idx % 2 != 0:
            sum_odd += int(digit)

    if sum_even == sum_odd:
        print(num, end=" ")
