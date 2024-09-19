budget = float(input())
number_vcard = int(input())
number_proc = int(input())
number_ram = int(input())

price_vc = 250
total_vc = number_vcard * price_vc
price_proc = (total_vc * 0.35) * number_proc
price_ram = (total_vc * 0.1) * number_ram

total_price = total_vc + price_proc + price_ram

if number_vcard > number_proc:
   total_price = total_price - (total_price * 0.15)

if budget >= total_price:
    print(f"You have {(budget-total_price):.2f} leva left!")
else:
    print(f"Not enough money! You need {(total_price-budget):.2f} leva more!")

