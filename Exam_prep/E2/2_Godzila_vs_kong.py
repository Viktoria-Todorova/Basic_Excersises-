budget = float(input())
statist = int(input())
clothing = float(input())
decor = budget * 0.1
total_clothes = statist * clothing

if statist > 150:
    total_clothes -= (total_clothes * 0.1)

total_money = decor + total_clothes

if total_money > budget:
    print("Not enough money!")
    print(f"Wingard needs {(total_money-budget):.2f} leva more.")
elif total_money <= budget:
    print("Action!")
    print(f"Wingard starts filming with {(budget-total_money):.2f} leva left.")