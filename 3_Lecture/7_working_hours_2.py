hour = int(input())
day = input()

if day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"] and 10 <= hour < 19:
    print("open")
else:
    print("closed")