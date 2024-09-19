volume_pool = int(input())
first_tube = int(input())
second_tube = int(input())
hours = float(input())

litres_from_first = first_tube * hours
litres_from_second = second_tube * hours
total = litres_from_first + litres_from_second

if total <= volume_pool:
    percent_pool = (total / volume_pool) * 100
    percent_first = (litres_from_first/total) * 100
    percent_second = (litres_from_second / total) * 100

    print(f"The pool is {percent_pool:.2f}% full. Pipe 1: {percent_first:.2f}%. Pipe 2: {percent_second:.2f}%.")
else:
    print(f"For {hours:.2f} hours the pool overflows with {(total-volume_pool):.2f} liters.")
