sum_available = 0

while True:
    data = input()
    if data == 'NoMoreMoney':
        break
    current_num = float(data)


    if current_num >= 0:
        sum_available += current_num
        print(f'Increase: {current_num:.2f}')
    else:
        print('Invalid operation!')
        break

print(f'Total: {sum_available:.2f}')









