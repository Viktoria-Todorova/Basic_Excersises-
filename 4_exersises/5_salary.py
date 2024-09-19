n_tabs = int(input())
salary = int(input())
#(flag = false) --2 metod za reshavane bez da se pravi proverga if
for tabs in range(n_tabs):
    name_tab = input()
    if name_tab == 'Facebook':
        salary -= 150
    elif name_tab == "Instagram":
        salary -= 100
    elif name_tab == "Reddit":
        salary -= 50
    if salary <= 0:
        print("You have lost your salary.")
        #(flag=true)
        break
if salary > 0: #if not flag
    print(salary)
