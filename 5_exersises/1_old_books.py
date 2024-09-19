searsh_book_name = input()
count = 0
while True:
    book_name = input()

    if book_name == "No More Books":
        break

    if searsh_book_name == book_name:
        print(f"You checked {count} books and found it.")
        break

    count += 1

if searsh_book_name != book_name:
    print("The book you search is not here!")
    print(f"You checked {count} books.")






