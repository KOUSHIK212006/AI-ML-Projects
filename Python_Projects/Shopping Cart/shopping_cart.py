
available = {"Monitor":300 , "Mouse" : 100 , "Keyboard" : 150 , "TV":500 , "Bag":250 , "Pen":60 , "Pencil":20} #Inventory
taken = {} #Cart 
state = -1 #For choice 
while True:
    state = int(input("Enter your choice : \t 1)Add \t 2)Remove \t 3)Calculate and display Bill \t 4)Check Cart \t 5)Exit\n"))
    

    if state not in (1,2,3,4,5):
        print("Please enter a valid choice")
        continue
        
    
    if state == 1:
        print("Available Products with price : " , available)
        item = input("Type the item to add : ")
        if item in available :
            taken[item] = available[item]
            print(item , "added successfully !")
        else:
            print("Failed to add ",item , "into Cart ")

    elif state == 2:
        item = input("Type the item to delete : ")
        if item in taken :
            taken.pop(item)
            print(item , "deleted successfully !")

        else:
            print("Failed to delete " , item , " from Cart ")

    elif state == 3:
        bill = 0
        for i in taken :
            bill += taken[i]
        print("The total bill is ", bill)

    elif state == 4:
        print(taken)

    elif state == 5:
        print("Exiting ....")
        break