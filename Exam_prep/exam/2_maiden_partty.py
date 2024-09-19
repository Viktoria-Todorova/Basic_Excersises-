total_price = float(input())
count_love_letters = int(input())
count_roses = int(input())
count_keychain = int(input())
count_caricature = int(input())
count_luckycharm = int(input())

total_count = count_roses +count_caricature + count_luckycharm +count_keychain+count_love_letters

price_love_letters = count_love_letters * 0.60
price_roses = count_roses * 7.20
price_keychain = count_keychain * 3.60
price_caricature = count_caricature * 18.2
price_luckycharm = count_luckycharm * 22

final = price_keychain + price_roses + price_luckycharm + price_caricature+price_love_letters

if total_count >= 25:
    final -= final * 0.35

extra_expenses = final * 0.1
final_money = final - extra_expenses

if final_money >= total_price:
    print(f"Yes! {(final_money-total_price):.2f} lv left.")
elif final_money < total_price:
    print(f"Not enough money! {(total_price-final_money):.2f} lv needed.")
