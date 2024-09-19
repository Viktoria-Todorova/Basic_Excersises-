from math import floor
from math import ceil

days = int(input())
kg_food = int(input())
food_dog_day_kg = float(input())
food_cat_day_kg = float(input())
food_turtle_day_gr = float(input())

food_dog = food_dog_day_kg * days
food_cat = food_cat_day_kg * days
food_turtle = (food_turtle_day_gr * days) / 1000

total_kg = food_dog + food_cat + food_turtle

if total_kg <= kg_food:
    food = kg_food - total_kg
    print(f"{floor(food)} kilos of food left.")

else:
    food_left = total_kg - kg_food
    print(f"{ceil(food_left)} more kilos of food are needed.")