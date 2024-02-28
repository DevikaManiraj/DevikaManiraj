contact = {}

def display_contact():
    print("Name\t\tContact Number")
    for key in contact:
        print("{}\t\t{}".format(key,contact.get(key)))
while True:
    choice = int(input("1. Add contact 2. Display Contact 3.Exit\n Please enter your choice: "))
    if choice == 1:
        id=input("Enter ID: ")
        name= input("Enter name: ")
        cell= input("Enter cell: ")
        email = input("Enter email: ")
        contact[name]= cell

    elif choice ==2:
            if not contact:
                print("Empty contact book")
            else:
                display_contact()

    else:
        break



