contacts={}
while True:

    print("1.ADD")
    print("2.Delete")
    print("3.Update")
    print("4.View")
    print("5.Search")
    print("6.Exit")

    choice=int(input("enter your choice:\n"))
    if choice==1:
        name=input("enter name:\n")
        if name in contacts:
            print("Contact Already exixts")
        else:
            phone_no=int(input("enter phone number:\n"))
            contacts[name]=phone_no
            print("contact added successfully")

    elif choice==2:
        name=input("enter name:\n")
        if name in contacts:
            contacts.pop(name)
            print("contact deleted successfully")
        else:
            print("contact not found")
    elif choice==3:
        name=input("enter name:\n")
        if name in contacts:
            new_phone_no=int(input("enter new phone number:\n"))
            contacts.update({name:new_phone_no})
            print("contact updated successfully")
        else:
            print("no contact found")
    elif choice==4:
        if len(contacts)==0:
            print("no contacts")
        else:
            for x,y in contacts.items():
                print(x,":",y)
    elif choice==5:
        name=input("enter name:\n")
        phone=contacts.get(name)
        if phone in contacts:
            print("Name: ",name)
            print("Phone: ",phone)
        else:
            print("no contact found")
    elif choice==6:
        print("thank you")
        break
    else:
        print("enter valid choice")
