from math import floor
from math import ceil


tennis_rocket = float(input())
number_rocket = int(input())
number_shoes = int(input())

price_shoes = tennis_rocket / 6

total_price = (price_shoes *number_shoes) + (tennis_rocket *number_rocket)

price_rest = total_price * 0.2

final_price_Djokovic = (total_price + price_rest)/8

final_price_sponsors = (total_price +price_rest) - final_price_Djokovic

print(f"Price to be paid by Djokovic {floor(final_price_Djokovic)}")
print(f"Price to be paid by sponsors {ceil(final_price_sponsors)}")