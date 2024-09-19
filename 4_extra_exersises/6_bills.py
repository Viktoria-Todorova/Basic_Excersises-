months = int(input())
water_bill = internet = electricity = others = percent = 0
for bills in range(months):
    bill_electricity = float(input())

    electricity += bill_electricity
    water_bill += 20
    internet += 15
    others = (electricity + water_bill + internet)
    percent = others + (others * 0.2)

average = (electricity + water_bill + internet + percent) / months

print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {percent:.2f} lv")
print(f"Average: {average:.2f} lv")
