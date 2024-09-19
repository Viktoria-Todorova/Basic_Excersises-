from math import floor
turnirs = int(input())
beggining_point = int(input())
average_points = 0
final = 0
wins = 0
for etap in range(turnirs):
    etap_reached = input()

    if etap_reached == "W":
        beggining_point += 2000
        average_points += 2000
        wins += 1
    elif etap_reached == "F":
        beggining_point += 1200
        average_points += 1200
    elif etap_reached == "SF":
        beggining_point += 720
        average_points += 720

final = average_points / turnirs #Средно спечелени точки за турнир:

print(f"Final points: {beggining_point}")
print(f"Average points: {floor(final)}")
print(f"{(wins/ turnirs * 100):.2f}%")
