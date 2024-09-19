town = input()
volume = float(input())
comission = 0
valid = True
if town == 'Sofia':
    if 0 <= volume <= 500:
        comission = volume * 0.05
    elif 500 < volume <= 1000:
        comission = volume * 0.07
    elif 1000 < volume <= 10000:
        comission = volume * 0.08
    elif volume > 10000:
        comission = volume * 0.12
    else:
        print("error")
        valid = False

elif town == 'Varna':
    if 0 <= volume <= 500:
        comission = volume * 0.045
    elif 500 < volume <= 1000:
        comission = volume * 0.075
    elif 1000 < volume <= 10000:
        comission = volume * 0.10
    elif volume > 10000:
        comission = volume * 0.13
    else:
        print("error")
        valid = False
elif town == 'Plovdiv':
    if 0 <= volume <= 500:
        comission = volume * 0.055
    elif 500 < volume <= 1000:
        comission = volume * 0.08
    elif 1000 < volume <= 10000:
        comission = volume * 0.12
    elif volume > 10000:
        comission = volume * 0.145
    else:
        print("error")
        valid = False

else:
    print("error")
    valid = False

if valid:
    print(f"{comission:.2f}")
