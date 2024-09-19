
ticket_student = ticket_standard = ticket_kid = total_tickets= 0
while True:
    name_movie = input()
    ticket_count = 0

    if name_movie == "Finish":
        break

    free_space = int(input())

    while True:
        ticket_type = input()

        if ticket_type == "End":
            break

        ticket_count +=1

        if ticket_type == "student":
            ticket_student +=1

        elif ticket_type == "standard":
            ticket_standard +=1

        elif ticket_type == "kid":
            ticket_kid +=1

        if ticket_count >= free_space:
            break

    total_tickets += ticket_count
    print(f"{name_movie} - {(ticket_count / free_space *100):.2f}% full.")

if total_tickets > 0:
    percent_students = ticket_student / total_tickets * 100
    percent_standard = ticket_standard / total_tickets * 100
    percent_kid = ticket_kid / total_tickets * 100

    print(f"Total tickets: {total_tickets}")
    print(f"{percent_students:.2f}% student tickets.")
    print(f"{percent_standard:.2f}% standard tickets.")
    print(f"{percent_kid:.2f}% kids tickets.")