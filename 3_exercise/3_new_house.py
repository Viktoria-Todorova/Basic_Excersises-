type_flower = input()
count_flower = int(input())
budget = int(input())
total = 0

if type_flower == "Roses":
    total = count_flower * 5
    if count_flower > 80:
        total = total - (total * 0.1)
elif type_flower == "Dahlias":
    total = count_flower * 3.8
    if count_flower > 90:
        total = total - (total * 0.15)
elif type_flower == "Tulips":
    total = count_flower * 2.8
    if count_flower > 80:
        total = total - (total * 0.15)
elif type_flower == "Narcissus":
    total = count_flower * 3
    if count_flower < 120:
        total = total + (total * 0.15)
elif type_flower == "Gladiolus":
    total = count_flower * 2.5
    if count_flower < 80:
        total = total + (total * 0.2)

if total <= budget :
    print(f"Hey, you have a great garden with {count_flower} {type_flower} and {(budget-total):.2f} leva left.")

else:
    print(f"Not enough money, you need {(total-budget):.2f} leva more.")

