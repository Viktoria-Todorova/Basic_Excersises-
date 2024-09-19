
sum_prime = sum_nonprime = 0
while True:
    non_prime = False

    number = input()
    if number == "stop":
        break

    current_num = int(number)

    if current_num < 0 :
        print("Number is negative.")
        continue
    elif current_num <=1:
        sum_nonprime += current_num
        non_prime =True

    else:
        for num in range(2,int(current_num ** 0.5) +1):
            if current_num % num == 0:
                sum_nonprime += current_num
                non_prime = True
                break

    if not non_prime:
        sum_prime +=current_num

print(f"Sum of all prime numbers is: {sum_prime}")
print(f"Sum of all non prime numbers is: {sum_nonprime}")

