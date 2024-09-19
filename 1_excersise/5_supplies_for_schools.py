
number_of_pens=int(input())
number_of_markers=int(input())
litres_for_cleaning=int(input())
percent_discount=int(input())
percent=percent_discount/100

price_pens=number_of_pens*5.8
price_markers=number_of_markers*7.2
price_cleaning=litres_for_cleaning*1.2

sum=price_pens+price_markers+price_cleaning
final_price=sum-(sum*percent)
print(final_price)
