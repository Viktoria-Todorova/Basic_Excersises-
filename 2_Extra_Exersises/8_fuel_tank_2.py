fuel = str(input())
litres_fuel = int(input())
club_card = str(input())

gasoline = 2.22
diesel = 2.33
gas = 0.93

if fuel == 'Gas':

    if 20 >= litres_fuel >= 25:
        if club_card == 'Yes':
            gas = 0.93 - 0.08
            total = gas * litres_fuel
        total = total - (total * 0.08)

    elif litres_fuel > 25:
        if club_card == 'Yes':
            gas = 0.93 - 0.08
            total = gas * litres_fuel
        total = total - (total * 0.10)

elif fuel == 'Gasoline':
    if 20 >= litres_fuel >= 25:
        if club_card == 'Yes':
            gasoline = 2.22 - 0.18
            total = gasoline * litres_fuel
        total = total - (total * 0.08)

    elif litres_fuel > 25:
        if club_card == 'Yes':
            gasoline = 2.22 - 0.18
            total = gasoline * litres_fuel
        total = total - (total * 0.10)


elif fuel == 'Diesel':
    if 20 >= litres_fuel >= 25:
        if club_card == 'Yes':
            diesel = 2.33 - 0.12
            total = diesel * litres_fuel
        total = total - (total * 0.08)

    elif litres_fuel > 25:
        if club_card == 'Yes':
            diesel = 2.33 - 0.12
            total = diesel * litres_fuel
        total = total - (total * 0.10)


print(total)



