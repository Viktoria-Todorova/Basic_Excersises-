n = int(input())

print('+ '+ '- ' * (n-2) + '+', end = " ")
print()
for i in range(n-2):
    print("| " + '- ' * (n-2) + '|', end =" ")
    print()
print('+ '+ '- ' * (n-2) + '+', end = " ")

print()