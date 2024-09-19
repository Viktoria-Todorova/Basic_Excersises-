num = int(input())
random = 1
for row in range(1, num +1):
    for side in range(1, row+1):
        if random > num:
            break

        print(random, end = ' ')
        random +=1
    print()