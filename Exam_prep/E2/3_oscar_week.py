movie_name = input()
type_room = input()
tickets = int(input())
ticket1 = 0
if movie_name == "A Star Is Born":
    if type_room == "normal":
        ticket1 += 7.5
    elif type_room == "luxury":
        ticket1 += 10.5
    elif type_room == "ultra luxury":
        ticket1 += 13.5

elif movie_name == "Bohemian Rhapsody":
    if type_room == "normal":
        ticket1 += 7.35
    elif type_room == "luxury":
        ticket1 += 9.45
    elif type_room == "ultra luxury":
        ticket1 += 12.75

elif movie_name == "Green Book":
    if type_room == "normal":
        ticket1 += 8.15
    elif type_room == "luxury":
        ticket1 += 10.25
    elif type_room == "ultra luxury":
        ticket1 += 13.25

elif movie_name == "The Favourite":
    if type_room == "normal":
        ticket1 += 8.75
    elif type_room == "luxury":
        ticket1 += 11.55
    elif type_room == "ultra luxury":
        ticket1 += 13.95

print(f"{movie_name} -> {(tickets * ticket1):.2f} lv.")