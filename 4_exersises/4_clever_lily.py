age = int(input())
price_washing_mashine = float(input())
price_toy = int(input())
savings = 0.0
count = 1
for n in range(1, age + 1):

    if n % 2 == 0:
        savings += count * 10
        savings -= 1
        count += 1
    elif n % 2 != 0:
        savings += price_toy

if savings >= price_washing_mashine:
    print(f"Yes! {(savings-price_washing_mashine):.2f}")
else:
    print(f"No! {(price_washing_mashine-savings):.2f}")
