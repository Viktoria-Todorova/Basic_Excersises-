etap = input()
type = input()
tickets = int(input())
picture = input()
price_picture = 0

if etap == "Quarter final":
    if type == "Standard":
        price = 55.5
    elif type == "Premium":
        price = 105.2
    elif type == "VIP":
        price = 118.9
elif etap == "Semi final":
    if type == "Standard":
        price = 75.88
    elif type == "Premium":
        price = 125.22
    elif type == "VIP":
        price = 300.4
elif etap == "Final":
    if type == "Standard":
        price = 110.1
    elif type == "Premium":
        price = 160.66
    elif type == "VIP":
        price = 400

total_price = price * tickets

if total_price > 4000 :
    if picture == "Y":
        total_price -= total_price*0.25
        final_price = total_price
elif 4000 >= total_price > 2500:
    total_price -= total_price * 0.1
    if picture == "Y":
        price_picture = 40
    final_price = total_price + (price_picture * tickets)
elif total_price <= 2500:
    if picture == "Y":
        price_picture = 40
    final_price = total_price + (price_picture * tickets)

print(f"{final_price:.2f}")






