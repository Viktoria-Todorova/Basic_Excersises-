n1 = int(input())
n2 = int(input())
operator = input()
even_or_not = ''

if operator == "+":
    result = n1 + n2
    if result % 2 == 0:
        even_or_not = 'even'
    else:
        even_or_not = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {even_or_not}")
elif operator == "-":
    result = n1 - n2
    if result % 2 == 0:
        even_or_not = 'even'
    else:
        even_or_not = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {even_or_not}")

elif operator == "*":
    result = n1 * n2
    if result % 2 == 0:
        even_or_not = 'even'
    else:
        even_or_not = 'odd'
    print(f"{n1} {operator} {n2} = {result} - {even_or_not}")

elif operator == "/":
    if n2 != 0:
        result = n1/n2
        print(f"{n1} / {n2} = {result:.2f}")
    else:
        print(f"Cannot divide {n1} by zero")
elif operator == "%":
    if n2 != 0:
        result = n1%n2
        print(f"{n1} % {n2} = {result}")
    else:
        print(f"Cannot divide {n1} by zero")


