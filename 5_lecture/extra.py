#Brute force attack

pin_password ='1234'
attempt = 0
guessed_password = ''

while guessed_password != pin_password:
    attempt +=1
    guessed_password = str(attempt)

    print(f'Attempt {attempt}: {guessed_password}')

    if guessed_password == pin_password:
        print(f'Pin password found {guessed_password}')
        break

print('Brute force attack finished!')