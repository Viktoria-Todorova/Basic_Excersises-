from sys import maxsize
num = int(input())
max_num = -maxsize
min_num = maxsize

for n in range(num):
    current_num = int(input())
    if current_num > max_num:
        max_num = current_num

    if current_num < min_num:
        min_num = current_num

print(f"Max number: {max_num}")
print(f"Min number: {min_num}")
