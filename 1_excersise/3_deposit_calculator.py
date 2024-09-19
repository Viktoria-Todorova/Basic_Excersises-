
deposit=int(input())
period_of_deposit=int(input())
year_percent=float(input())
percent=year_percent/100
sum=deposit+period_of_deposit*((deposit*percent)/12)

print(sum)