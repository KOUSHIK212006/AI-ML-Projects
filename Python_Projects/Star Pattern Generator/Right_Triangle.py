#Right triangle 
n = int(input("Enter the number of rows : "))
m=1
for i in range(n):
    for j in range(m):
        print("*",end = " ")
    m+=1
    print()