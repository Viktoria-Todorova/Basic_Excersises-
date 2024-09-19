visitors = int(input())
back = chest = legs =abs = protein_shake = protein_bar =0
people_train = people_buy = 0
for every_visitor in range(visitors):
    activity = input()

    if activity == "Back":
        back +=1
        people_train +=1
    elif activity == "Chest":
        chest +=1
        people_train += 1
    elif activity == "Legs":
        legs +=1
        people_train += 1
    elif activity == "Abs":
        abs +=1
        people_train += 1
    elif activity == "Protein shake":
        protein_shake += 1
        people_buy += 1
    elif activity == "Protein bar":
        protein_bar +=1
        people_buy += 1
print(f"{back} - back")
print(f"{chest} - chest")
print(f"{legs} - legs")
print(f"{abs} - abs")
print(f"{protein_shake} - protein shake")
print(f"{protein_bar} - protein bar")
print(f"{(people_train/visitors*100):.2f}% - work out")
print(f"{(people_buy/visitors*100):.2f}% - protein")


