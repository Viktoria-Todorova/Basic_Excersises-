num1 = int(input())
num2 = int(input())
magic_num = int(input())
count = 0
flag = False
for i in range (num1, num2 +1):
    for j in range(num1, num2 +1):
        count +=1
        if i + j == magic_num:
            print(f"Combination N:{count} ({i} + {j} = {magic_num})")
            flag = True
            break
    if flag:
        break
if not flag:
    print(f"{count} combinations - neither equals {magic_num}")

