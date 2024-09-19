minutes = int(input())
seconds = int(input())
distance = float(input())
sec_per100_meters = int(input())

total_seconds = seconds + (minutes * 60)
slowing = (distance / 120) * 2.5
total_time = (distance/100 * sec_per100_meters) -slowing


if total_seconds >= total_time:
    print("Marin Bangiev won an Olympic quota!")
    print(f"His time is {total_time:.3f}.")
else:
    print( f"No, Marin failed! He was {(total_time-total_seconds):.3f} second slower.")

