
n_km = int(input())
when = str(input())

taxi_start = 0.7
taxi_day_km = 0.79
taxi_night_km = 0.9

bus_price = 0.09
train_price = 0.06

if n_km < 20:
    if when == "day":
        total = taxi_start + (taxi_day_km * n_km)
        print(f"{total:.2f}")
    else:
        total = taxi_start + (taxi_night_km * n_km)
        print(f"{total:.2f}")
elif 20 <= n_km < 100:
    total = bus_price * n_km
    print(f"{total:.2f}")
else:
    total = train_price * n_km
    print(f"{total:.2f}")





