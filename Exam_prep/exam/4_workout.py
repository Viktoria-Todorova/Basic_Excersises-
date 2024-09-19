from math import ceil
n = int(input())

m = float(input())
dayly_km = m
total_km = 0
for every_day in range(1, n + 1):
    today_percent = int(input())

    dayly_km += dayly_km * (today_percent/100)
    total_km += dayly_km

final_km = m + total_km

if final_km < 1000 :
    print(f"Sorry Mrs. Ivanova, you need to run {ceil(1000-final_km)} more kilometers")
elif final_km >= 1000 :
    print(f"You've done a great job running {ceil(final_km-1000)} more kilometers!")


