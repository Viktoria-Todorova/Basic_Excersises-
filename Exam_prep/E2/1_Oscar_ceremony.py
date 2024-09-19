rent = int(input())

statues = rent- (rent * 0.3)
catering = statues-(statues * 0.15)
sound = catering /2
total = statues + catering + sound + rent

print(f"{total:.2f}")
