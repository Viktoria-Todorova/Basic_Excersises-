from math import floor
w_in_m = float(input())
h_in_m = float(input())

if 3 <= h_in_m <= w_in_m <= 100:
    w_in_cm = w_in_m*100
    h_in_cm = h_in_m*100

    tables_per_w = (w_in_cm)//120
    tables_per_h = (h_in_cm-100)//70

    total = ((tables_per_w * tables_per_h)-3)

print(total)
