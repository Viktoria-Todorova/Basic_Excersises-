#generirane na paroli v saitovete

import random
import string

ascii_letters = string.ascii_letters
digits = string.digits
special_chars = string.punctuation

pasword_lenght = int(input('Enter the desired password lenght:'))

password = ''
all_characters =  ascii_letters + digits + special_chars


for i in range(pasword_lenght):
    password += random.choice(all_characters)

print(f'Generated pasword:{password}')

