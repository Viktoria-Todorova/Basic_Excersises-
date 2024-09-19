money_needed = float(input())
money_have = float(input())
spend_count = save_count = 0
while True:
    activity = input()
    money = float(input())
    save_count +=1
    if activity == "save":
        money_have += money
        spend_count = 0

    elif activity == "spend":
        money_have -= money
        spend_count += 1
        if money_have < 0 :
            money_have = 0

    if spend_count == 5:
        print("You can't save the money.")
        print(f"{save_count}")
        break
    if money_have >= money_needed:
        print(f"You saved the money for {save_count} days.")
        break







