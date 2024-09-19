weight = int(input())
bus_price = truck_price = train_price = 0
percent_bus =0
total_ton_bus = total_ton_truck = total_ton_train =0
for every_weight in range(0, weight):
    ton_weight = int(input())

    if ton_weight <= 3:
        bus_price += 200 * ton_weight
        total_ton_bus += ton_weight
    elif 4 <= ton_weight <= 11:
        truck_price += 175 * ton_weight
        total_ton_truck += ton_weight
    elif ton_weight >= 12:
        train_price += 120 * ton_weight
        total_ton_train += ton_weight
total_ton = (total_ton_bus + total_ton_truck + total_ton_train)
total_price = (bus_price + truck_price + train_price)/total_ton

print(f"{total_price:.2f}")
print(f"{(total_ton_bus/total_ton*100):.2f}%")
print(f"{(total_ton_truck/total_ton*100):.2f}%")
print(f"{(total_ton_train/total_ton*100):.2f}%")