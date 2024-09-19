days = int(input())
type_room = input()
grade = input()
nights = days -1
room_for_one = 18
apartmaent = 25
president = 35
final_price = 0

if type_room == "apartment":
    final_price = nights * apartmaent
    if days < 10:
        final_price -= final_price * 0.3
    elif 10 <= days < 15:
        final_price -= final_price *0.35
    elif days > 15:
        final_price -= final_price * 0.5
elif type_room == "president apartment":
    final_price = nights * president
    if days < 10:
        final_price -= final_price * 0.1
    elif 10 <= days < 15:
        final_price -= final_price *0.15
    elif days > 15:
        final_price -= final_price * 0.2

elif type_room == "room for one person":
    final_price = nights * room_for_one

if grade == "positive" :
    final_price += final_price * 0.25
elif grade == "negative":
    final_price -= final_price * 0.1

print(f"{final_price:.2f}")




