price_of_veggies=float(input())
price_of_fruits=float(input())
kg_of_veggies=int(input())
kg_of_fruits=int(input())

total_price_veggie=price_of_veggies*kg_of_veggies
total_price_fruits=price_of_fruits*kg_of_fruits

price_in_euro=(total_price_veggie+total_price_fruits)/1.94

print('%.2f'%price_in_euro)

