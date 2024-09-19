days = int(input())
hours = int(input())
tax= 0

for day in range(1, days + 1):
    tax_per_day = 0
    for hour in range(1,hours +1):

        if day %2 == 0:
            if hour %2 != 0:
                tax += 2.5
                tax_per_day +=2.5
            else:
                tax +=1
                tax_per_day += 1
        elif day %2 != 0:
            if hour %2 == 0:
                tax += 1.25
                tax_per_day += 1.25
            else:
                tax +=1
                tax_per_day += 1

    print(f"Day: {day} - {tax_per_day:.2f} leva")
print(f"Total: {tax:.2f} leva")
