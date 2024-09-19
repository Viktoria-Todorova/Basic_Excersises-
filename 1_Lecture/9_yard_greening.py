sq_meters_for_landcaping=float(input())
price_for_landcaping=sq_meters_for_landcaping*7.61
discount=price_for_landcaping*0.18
total=price_for_landcaping-discount

print(f"The final price is: {total} lv.")
print(f"The discount is: {discount} lv.")
