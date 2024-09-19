hour = int(input())
minutes = int(input())

hour_in_minutes = hour * 60
total_minutes = hour_in_minutes + minutes
minutes_plus_15 = total_minutes + 15


hour_final = minutes_plus_15 // 60 % 24
minutes_final = minutes_plus_15 % 60

if minutes_final < 10:
    print(f"{hour_final}:0{minutes_final}")
else:
    print(f"{hour_final}:{minutes_final}")


