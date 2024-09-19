day_offs = int(input())

playtime_on_day_off = day_offs * 127
workdays = 365 - day_offs
playtime_on_workdays = workdays * 63
total = playtime_on_workdays + playtime_on_day_off

if total < 30000:
    difference = 30000 - total
    hours = difference // 60
    minutes = difference % 60
    print("Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")

else:
    difference = total - 30000
    hours = difference // 60
    minutes = difference % 60
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")

