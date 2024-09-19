number = int(input())
p1 = p2 = p3 = p4 = p5 = 0

for num in range(number):
    current_num = int(input())
    if current_num < 200:
        p1 += 1
    elif 200 <= current_num < 400:
        p2 += 1
    elif 400 <= current_num < 600:
        p3 += 1
    elif 600 <= current_num < 800:
        p4 += 1
    elif current_num >= 800:
        p5 += 1

print(f"{(p1/number * 100):.2f}%")
print(f"{(p2/number * 100):.2f}%")
print(f"{(p3/number * 100):.2f}%")
print(f"{(p4/number * 100):.2f}%")
print(f"{(p5/number * 100):.2f}%")
