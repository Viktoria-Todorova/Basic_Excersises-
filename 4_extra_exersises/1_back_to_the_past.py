price = float(input())
year_living = int(input())
years = 18
final_sum = 0
for year in range(1800, year_living + 1):

    if year % 2 == 0:
        price -= 12000
        years += 1
    elif year % 2 != 0:
        price -= 12000 + (50 * years)
        years += 1

if price >= 0:
    print(f"Yes! He will live a carefree life and will have {(price):.2f} dollars left.")
else:
    print(f"He will need {abs(price-final_sum):.2f} dollars to survive.")
