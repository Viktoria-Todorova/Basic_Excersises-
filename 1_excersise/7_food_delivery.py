
number_of_chicken_menu=int(input())
number_of_fish_menu=int(input())
number_of_vegatarian_menu=int(input())

price_of_chicken=number_of_chicken_menu*10.35
price_of_fish=number_of_fish_menu*12.4
price_of_veg=number_of_vegatarian_menu*8.15
price_of_delivery=2.5

total_price=price_of_chicken+price_of_fish+price_of_veg
price_of_desert=total_price*0.2

final_price_of_order=total_price+price_of_desert+price_of_delivery

print(final_price_of_order)