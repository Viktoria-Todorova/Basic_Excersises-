expected_sum = float(input())
count = money_count_cash=money_count_card =count_cash = count_card =total_sum =0
while True:
    command = input()

    if command == "End":
        if total_sum < expected_sum:
            print(f"Failed to collect required money for charity.")
            break

    price = int(command)
    count +=1

    if count %2 != 0:
        if price > 100:
            print("Error in transaction!")
        else:
            money_count_cash += price
            count_cash +=1
            total_sum += price
            print("Product sold!")

    else:
        if price < 10:
            print("Error in transaction!")
        else:
            money_count_card += price
            count_card +=1
            total_sum += price
            print("Product sold!")

        if total_sum >= expected_sum:
            if count_cash > 0:
                average_cash = money_count_cash / count_cash
            else:
                average_cash = 0.00
            if count_card >0:
                average_card = money_count_card / count_card
            else:
                average_card = 0.00

            print(f"Average CS: {average_cash:.2f}")
            print(f"Average CC: {average_card:.2f}")
            break








