budged = float(input())
people = int(input())
price_per_person = float(input())

decor_price = budged * 0.1

if people > 150:
    price_per_person = price_per_person - (price_per_person * 0.1)

final_price = people * price_per_person
total_price = final_price + decor_price

if total_price > budged:
    print("Not enough money!")
    print(f"Wingard needs {(total_price-budged):.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {(budged-total_price):.2f} leva left.")

