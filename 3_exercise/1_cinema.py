type_movie = input()
rows = int(input())
column = int(input())


total = rows * column
income = 0
if type_movie == 'Premiere' :
    income = 12 * total
elif type_movie == 'Normal':
    income = 7.5 * total
elif type_movie == 'Discount':
    income = 5 * total

print (f"{income:.2f} leva")

