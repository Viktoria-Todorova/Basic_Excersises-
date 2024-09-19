hour_exam = int(input())
minutes_exam = int(input())

hour_arrive = int(input())
minutes_arrive = int(input())

hour_to_minutes_exam = hour_exam * 60
hour_to_minutes_arrive = hour_arrive * 60

total_exam = minutes_exam + hour_to_minutes_exam
total_arrive = minutes_arrive + hour_to_minutes_arrive
difference = total_arrive - total_exam
hour = 0
minutes = 0
ddifference = 0

if difference == 0:
    print("On time")

elif difference < 0:
    ddifference = abs(difference)
    if 1 <= ddifference <= 30:
        if ddifference >= 1:
            print("On time")
            print(f"{ddifference} minutes before the start")

    elif 30 <= ddifference <= 59:
        print("Early")
        print(f"{ddifference} minutes before the start")
    elif ddifference >= 60:
        hours = ddifference // 60
        minutes = ddifference % 60
        if minutes < 10:
            print("Early")
            print(f"{hours}:0{minutes} hours before the start")
        else:
            print("Early")
            print(f"{hours}:{minutes} hours before the start")

elif difference > 0:
    if 1 <= difference <= 59:
        print("Late")
        print(f"{difference} minutes after the start")

    else:
        hours = difference // 60
        minutes = difference % 60
        if minutes < 10:
            print("Late")
            print(f"{hours}:0{minutes} hours after the start")
        else:
            print("Late")
            print(f"{hours}:{minutes} hours after the start")









