import random ,string

digits = list(string.digits)
interation_counter = 0
guess_password = ''
password = input('Enter your pin code here:')

while guess_password != password:
    guess_password = random.choices(digits, k=len(password))
    interation_counter += 1
    print(f">>>>>{''.join(guess_password)}<<<<<")

    if guess_password == list(password):
        print(f'Your password is {"".join(guess_password)}')
        print(f'Number of irretations is :{interation_counter}')
        break
