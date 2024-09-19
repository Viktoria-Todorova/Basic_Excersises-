wins = loses = 0
total_games = 0
while True:
    name_turnir = input()
    game = 0

    if name_turnir == "End of tournaments":
        print(f"{(wins / total_games * 100):.2f}% matches win")
        print(f"{(loses / total_games * 100):.2f}% matches lost")
        break

    count_turnirs = int(input())

    for mach in range(count_turnirs):
        desi_points = int(input())
        other_points = int(input())
        game += 1
        total_games += 1

        if desi_points > other_points:
            wins +=1
            print(f"Game {game} of tournament {name_turnir}: win with {desi_points-other_points} points.")
            continue
        elif desi_points < other_points:
            loses +=1
            print(f"Game {game} of tournament {name_turnir}: lost with {other_points-desi_points} points.")
            continue


