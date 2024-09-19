from sys import maxsize
number = int(input())
max_num = -maxsize #pishem s minus za da e po-lesna proverkata
sum_num = 0

for num in range(number):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num
    sum_num += current_num

if max_num == (sum_num - max_num): #mahame max_num zashoto to go e sumiralo vav for cikula
    print('Yes')
    print(f'Sum = {max_num}')
else:
    print("No")
    print(f"Diff = {abs(max_num - (sum_num - max_num))}") #za da pokajem razliakta mejdu maksimalnata stoinost i sumata bez maks stoinost


