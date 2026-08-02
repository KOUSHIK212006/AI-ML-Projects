contacts={}
while True:
    print("1.Add Contact")
    print("2.update phone number")
    print("3.delete contact")
    print("4.display contact")

    choice=int(input("Enter your choice:\n"))

    match choice:
        case 1: 
            name=input("Enter name\n")
            if name in contacts:
                print("contact already exists")
            else:
                phoneno=int(input("enter phone number\n"))
                contacts[name]=phoneno
                print("contact added successfully")
    

        case 2:
            name=input("enter name\n")
            if name in contacts:
                new_phoneno=int(input("enter new phone number\n"))
                contacts[name]=new_phoneno
                print("contact updated successfully")
            else:
                print("no contact found")
  

        case 3:
            name=input("enter name\n")
            if name in contacts:
                del contacts[name]
                print("deleted contact successfully")
            else:
                print("contact not found")
   

        case 4:
            if len(contacts)==0:
                print("no contacts")
            else:
                print("\nContacts:")
                for x,y in contacts.items():
                    print(x,":",y)
            break
        case _:
            print("Invalid choice")
    