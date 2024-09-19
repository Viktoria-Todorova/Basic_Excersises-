money = float(input())
coins_count = 0
while money > 0:


    if money >= 2:
        money -= 2
        coins_count += 1
    elif 2 > money >= 1:
        money -= 1
        coins_count += 1
    elif 1 > money >= 0.5:
        money -= 0.5
        coins_count +=1
    elif 0.5 > money >= 0.2:
        money -= 0.2
        coins_count += 1
    elif 0.2 > money >= 0.1:
        money -= 0.1
        coins_count += 1
    elif 0.1 > money >= 0.05:
        money -= 0.05
        coins_count +=1
    elif 0.05 > money >= 0.02:
        money -= 0.02
        coins_count += 1
    elif money < 0.02:
        money -= 0.01
        coins_count +=1
    money = round(money , 2) #zashotto ostava niakakyv ostatuk ot python i pravi tazi grehska

print(coins_count)
