from sys import maxsize
from math import floor
max_num = -maxsize
current_word = ''
current_points = 0
while True:
    text = str(input())
    total = 0
    count = 0

    if text == "End of words":
        break

    for i in range(len(text)):
        total += ord(text[i])
        count += 1

    if text[0].lower() in {'a', 'e', 'i', 'o', 'u', 'y'}:
        final = total * count
    else:
        final = total / count
    current_points = int(final)

    if current_points > max_num:
        max_num = current_points
        current_word = text

print(f"The most powerful word is {current_word} - {floor(max_num)}")


