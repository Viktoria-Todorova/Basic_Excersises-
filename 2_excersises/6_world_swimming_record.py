from math import floor
record_per_second = float(input())
distance_in_meters = float(input())
time_per_meter = float(input())

second = distance_in_meters * time_per_meter
slow = floor(distance_in_meters/15)
#slow = (distance_in_meters/15) * 12.5 //1
total_slow = slow * 12.5
total_time = second + total_slow


if total_time >= record_per_second:
    print(f"No, he failed! He was {(total_time - record_per_second):.2f} seconds slower.")

else:
    print(f" Yes, he succeeded! The new world record is {total_time:.2f} seconds.")
