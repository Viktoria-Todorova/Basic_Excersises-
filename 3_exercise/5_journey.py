budget = float(input())
season = input()
location = ""
where = ""

if budget <= 100:
    location = "Bulgaria"
    if season == "summer":
        where = "Camp"
        budget -= (budget * 0.7)
    elif season == "winter":
        where = "Hotel"
        budget -= (budget * 0.3)
elif budget <= 1000:
    location = "Balkans"
    if season == "summer":
        where = "Camp"
        budget -= (budget * 0.6)
    elif season == "winter":
        where = "Hotel"
        budget -= (budget * 0.2)
elif budget > 1000:
    location = "Europe"
    where = "Hotel"
    budget -= (budget * 0.1)

print(f"Somewhere in {location}")
print(f"{where} - {(budget):.2f}")

