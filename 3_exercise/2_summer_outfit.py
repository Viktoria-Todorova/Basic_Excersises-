gradus = int(input())
when = input()
Outfit = ""
Shoes = ""
if when == "Morning":
    if 10 <= gradus <= 18:
        Outfit = 'Sweatshirt'
        Shoes = 'Sneakers'
    elif 18 < gradus <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    else:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'

elif when == "Afternoon":
    if 10 <= gradus <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < gradus <= 24:
        Outfit = 'T-Shirt'
        Shoes = 'Sandals'
    else:
        Outfit = 'Swim Suit'
        Shoes = 'Barefoot'

elif when == "Evening":
    if 10 <= gradus <= 18:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    elif 18 < gradus <= 24:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'
    else:
        Outfit = 'Shirt'
        Shoes = 'Moccasins'

print(f"It's {gradus} degrees, get your {Outfit} and {Shoes}.")
