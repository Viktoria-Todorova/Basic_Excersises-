wins = loses = even = 0

for i in range(0,3):
    result = input()
    home_goals, away_goals = map(int, result.split(":"))
    if home_goals > away_goals:
        wins +=1
    elif home_goals < away_goals:
        loses +=1
    elif home_goals == away_goals:
        even +=1

print(f"Team won {wins} games.")
print(f"Team lost {loses} games.")
print(f" Drawn games: {even}")