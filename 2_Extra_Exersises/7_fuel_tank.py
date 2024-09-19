fuel = str(input())
litres_fuel = int(input())

if fuel == "Diesel" or fuel == "Gasoline" or fuel == "Gas":
    if litres_fuel >= 25:
        print(f"You have enough {fuel[0].lower() + fuel[1:]}.")
    else:
        print(f"Fill your tank with {fuel[0].lower() + fuel[1:]}!")
else:
    print("Invalid fuel!")
