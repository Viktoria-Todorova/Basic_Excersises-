n = int(input())
current = 1
for i in range(1, n+1):
    for j in range (1,i+1):
        if current > n:
            break

        print(current, end =" ")
        current +=1
    print()
