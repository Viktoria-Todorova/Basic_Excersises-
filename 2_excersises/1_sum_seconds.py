first_time = int(input())
second_time = int(input())
third_time = int(input())

total_time_seconds = first_time + second_time + third_time

minutes = total_time_seconds // 60
seconds = total_time_seconds % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
