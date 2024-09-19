days_staying = int(input())
type_room = input()
rating = input()
nights_staying = days_staying - 1

price_room_for_one = 18.00
price_apartment = 25.00
price_president = 35.00

total_price = 0

if type_room == "room for one person":
    total_price = nights_staying * price_room_for_one

elif type_room == "apartment":
    total_price = nights_staying * price_apartment
    if nights_staying <= 10:
        total_price -= total_price * 0.3
    elif 10 < nights_staying < 15:
        total_price -= total_price * 0.35
    elif nights_staying >= 15:
        total_price -= total_price * 0.5

elif type_room == "president apartment":
    total_price = nights_staying * price_president
    if nights_staying <= 10:
        total_price -= total_price * 0.1
    elif 10 < nights_staying < 15:
        total_price -= total_price * 0.15
    elif nights_staying >= 15:
        total_price -= total_price * 0.2

if rating == "positive":
    total_price += total_price * 0.25
elif rating == "negative":
    total_price -= total_price * 0.1

print(f"{total_price:.2f}")