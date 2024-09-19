from math import floor
turnir = int(input())
points_in_start = int(input())
points = wins = 0
for every_turnir in range(turnir):
    etap = input()

    if etap == "W":
        points += 2000
        wins += 1
    elif etap == "F":
        points += 1200
    elif etap == "SF":
        points += 720

average_points = points / turnir
average_turnirs = wins / turnir * 100
print(f"Final points: {points + points_in_start}")
print(f"Average points: {floor(average_points)}")
print(f"{average_turnirs:.2f}%")



