capacity = int(input())
total_fans = int(input())
fans_a = fans_b = fans_v = fans_g =0
percent_a = percent_b = percent_v = percent_g = 0
for all_fans in range(total_fans):
    sector = str(input())

    if sector == "A":
        fans_a += 1
        percent_a = fans_a / total_fans * 100
    elif sector == "B":
        fans_b += 1
        percent_b = fans_b / total_fans * 100
    elif sector == "V":
        fans_v += 1
        percent_v = fans_v / total_fans * 100
    elif sector == "G":
        fans_g += 1
        percent_g = fans_g / total_fans * 100

total_percent = total_fans /capacity *100

print(f"{percent_a:.2f}%")
print(f"{percent_b:.2f}%")
print(f"{percent_v:.2f}%")
print(f"{percent_g:.2f}%")
print(f"{total_percent:.2f}%")