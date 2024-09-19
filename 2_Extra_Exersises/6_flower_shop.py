from math import ceil
from math import floor
n_magnolia = int(input())
n_ziumbiul = int(input())
n_rose = int(input())
n_cactus = int(input())
price_gift = float(input())

price_magnolia = n_magnolia * 3.25
price_ziumbiul = n_ziumbiul * 4
price_rose = n_rose * 3.5
price_cactus = n_cactus * 8
total = price_magnolia + price_ziumbiul + price_rose + price_cactus
percent = total * 0.05
final = total - percent


if final >= price_gift:
    print(f"She is left with {floor(final-price_gift)} leva.")
else:
    print(f"She will have to borrow {ceil(price_gift-final)} leva.")

