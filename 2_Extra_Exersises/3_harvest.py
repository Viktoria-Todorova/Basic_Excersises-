from math import floor
from math import ceil

x_vineyard = int(input())
y_grapes = float(input())
z_litres_wine = int(input())
workers = int(input())

total_grapes = x_vineyard * y_grapes
wine = (total_grapes * 0.4) / 2.5
wine_left = wine - z_litres_wine
wine_per_worker = wine_left / workers
if wine < z_litres_wine:
    print(f"It will be a tough winter! More {floor(z_litres_wine-wine)} liters wine needed.")

else:
    print(f"Good harvest this year! Total wine: {floor(wine)} liters.")
    print(f"{ceil(wine_left)} liters left -> {ceil(wine_per_worker)} liters per person.")