year_tax = int(input())
shoes = year_tax - (year_tax * 0.4)
clothes = shoes - (shoes * 0.2)
ball = clothes / 4
accessories = ball / 5

total = shoes + clothes + ball + accessories +year_tax
print(f"{total:.2f}")