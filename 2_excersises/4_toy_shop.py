price_excursion = float(input())
number_of_puzzles = int(input())
number_of_dolls = int(input())
number_of_teddies = int(input())
number_of_minions = int(input())
number_of_trucks = int(input())

price_puzzles = number_of_puzzles * 2.6
prize_dolls = number_of_dolls * 3
price_teddies = number_of_teddies * 4.1
price_minions = number_of_minions * 8.2
price_trucks = number_of_trucks * 2

total_number_of_toys = number_of_trucks + number_of_teddies + number_of_minions + number_of_dolls + number_of_puzzles

total_price = price_puzzles + prize_dolls + price_teddies + price_minions + price_trucks


if total_number_of_toys >= 50:
    total_price = total_price - (total_price * 0.25)

final_price = (total_price - (total_price * 0.1))

if final_price >= price_excursion:
    print(f"Yes! {(final_price-price_excursion):.2f} lv left.")
else:
    print(f"Not enough money! {(price_excursion-final_price):.2f} lv needed.")




