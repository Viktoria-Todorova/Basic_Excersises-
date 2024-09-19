budget = float(input())
category = input()
people = int(input())

final_budget = 0
money_left = 0
if 1 <= people <= 4:
    final_budget = budget * 0.25 #tolkova pari ostavat za tova e obratnoto na zadachata
elif 5 <= people <= 9:
    final_budget = budget * 0.40
elif 10 <= people <= 24:
    final_budget = budget * 0.50
elif 25 <= people <= 49:
    final_budget = budget * 0.60
elif people >= 50:
    final_budget = budget * 0.75

if category == 'VIP':
    money_left = final_budget - (people * 499.99)
elif category == 'Normal':
    money_left = final_budget - (people * 249.99)

if money_left >= 0:
    print(f"Yes! You have {money_left:.2f} leva left.")
elif money_left < 0:
    money = abs(money_left)
    print(f"Not enough money! You need {money:.2f} leva.")
