days_count = 1
m_count = 5364
while True:
    yes_or_no = input()

    if yes_or_no == "END":
        print("Failed!")
        print(f"{m_count}")
        break

    metres = int(input())

    if m_count < 8848:
        if yes_or_no == "Yes":
            days_count +=1

        if days_count > 5:
            print("Failed!")
            print(f"{m_count}")
            break

        m_count += metres

    if m_count >= 8848:
        print(f"Goal reached for {days_count} days!")
        break








