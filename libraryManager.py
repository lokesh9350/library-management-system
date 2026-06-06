def menu():
    print("\n" * 2)

    print("===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")


def add_book(ids, names, authors):
    bid = input("Enter Book ID: ")
    bname = input("Enter Book Name: ")
    author = input("Enter Author Name: ")

    ids.append(bid)
    names.append(bname)
    authors.append(author)

    print("Book Added Successfully")


def view_books(ids, names, authors):
    if len(ids) == 0:
        print("No Books Available")
        return

    print("\n===== BOOK LIST =====")

    for i in range(len(ids)):
        print(f"\nBook {i+1}")
        print("Book ID    :", ids[i])
        print("Book Name  :", names[i])
        print("Author     :", authors[i])


def main():
    ids = []
    names = []
    authors = []

    while True:
        menu()

        ch = int(input("Enter Choice: "))

        if ch == 1:
            add_book(ids, names, authors)

        elif ch == 2:
            view_books(ids, names, authors)

        elif ch == 3:
            print("Thank You")
            break

        else:
            print("Invalid Choice")


if __name__ == "__main__":
    main()
