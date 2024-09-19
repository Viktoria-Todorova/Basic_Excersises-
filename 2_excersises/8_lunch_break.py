from math import ceil
name_of_movie = str(input())
time_ep = int(input())
time_break = int(input())

time_lunch = time_break/8
time_breath = time_break/4
time_left = time_break - time_lunch - time_breath

if time_left >= time_ep:
    print(f"You have enough time to watch {name_of_movie} and left with {ceil(time_left-time_ep)} minutes free time.")
else:
    print(f"You don't have enough time to watch {name_of_movie}, you need {ceil(time_ep-time_left)} more minutes.")