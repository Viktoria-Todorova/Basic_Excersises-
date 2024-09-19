a1 = int(input())
a2 = int(input())
n = int(input())
p = int(n/2)
first = ''
second= third = forth = 0
for symbol1 in range(a1, a2):
    if symbol1 %2 != 0:
        first = chr(symbol1)
    else:
        continue
    for symbol2 in range(1,n):
        second = symbol2

        for symbol3 in range(1,p):
            third = symbol3

            for symbol4 in range(ord(first)+1):
                forth = symbol4

            sum_all = second + third + forth

            if sum_all %2 !=0:
                print(f"{first}-{second}{third}{forth}")
            else:
                continue


