budget = int(input())
season = input()
fishers = int(input())
price_boat = 0

if season == "Spring":
    price_boat = 3000
    if fishers <= 6:
        price_boat = price_boat - (price_boat * 0.1)
    elif 7 < fishers <= 11:
        price_boat = price_boat - (price_boat * 0.15)
    else:
        price_boat = price_boat - (price_boat * 0.25)

elif season == "Summer" or season == "Autumn":
    price_boat = 4200
    if fishers <= 6:
        price_boat = price_boat - (price_boat * 0.1)
    elif 7 < fishers <= 11:
        price_boat = price_boat - (price_boat * 0.15)
    else:
        price_boat = price_boat - (price_boat * 0.25)

elif season == "Winter":
    price_boat = 2600
    if fishers <= 6:
        price_boat = price_boat - (price_boat * 0.1)
    elif 7 < fishers <= 11:
        price_boat = price_boat - (price_boat * 0.15)
    else:
        price_boat = price_boat - (price_boat * 0.25)

if fishers % 2 == 0 and season != "Autumn":
    price_boat = price_boat - (price_boat * 0.05)

if price_boat <= budget:
    print(f"Yes! You have {(budget-price_boat):.2f} leva left.")
else:
    print(f"Not enough money! You need {(price_boat-budget):.2f} leva.")
