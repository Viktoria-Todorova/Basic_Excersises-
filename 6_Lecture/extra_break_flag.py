flag = False

for h in range (24):
    for m in range(60):
        if h == 5 and m == 1:
            flag = True
            break
        print(f"{h}:{m}")
    if flag:
        break