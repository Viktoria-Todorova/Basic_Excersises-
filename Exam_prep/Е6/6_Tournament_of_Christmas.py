days = int(input())
money = wins = lose = 0
for i in range(days):
    money_per_day = 0
    wins_per_day = loses_per_day = 0
    while True:
        sport = input()

        if sport == "Finish":
            break

        result = input()

        if result == "win":
            wins += 1
            wins_per_day +=1
            money_per_day += 20
        elif result == "lose":
            lose += 1
            loses_per_day +=1

    if wins_per_day > loses_per_day:
        money_per_day += money_per_day * 0.1

    money += money_per_day

if wins > lose:
    money += money * 0.2
    print(f"You won the tournament! Total raised money: {money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {money:.2f}")






