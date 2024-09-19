
while True:
    country = input()
    if country == "End":
        break

    budget = float(input())
    saved_money = 0

    while saved_money < budget:
        total = float(input())
        saved_money += total

    print(f"Going to {country}!")



