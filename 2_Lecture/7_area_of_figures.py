
from math import pi

geometric_figure = str(input())

total=0

if geometric_figure == 'square':
    first_number = float(input())
    total = first_number*first_number

elif geometric_figure == 'rectangle':
    first_number = float(input())
    second_number = float(input())
    total = first_number*second_number

elif geometric_figure == 'circle':
    first_number = float(input())
    total = pi * (first_number ** 2)

elif geometric_figure == 'triangle':
    first_number = float(input())
    second_number = float(input())
    total = (first_number*second_number)/2

print(f"{total:.3f}")



