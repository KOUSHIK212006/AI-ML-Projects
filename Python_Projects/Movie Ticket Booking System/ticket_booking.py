age = int(input("Please Enter your age : "))
student = input("are u a student (y/n) ? :")
weekend = input("Is the booking for weekend(y/n) ? :")
VIP = input("Do u want VIP Tickets ( y/n) ? :")

base = 150
child_disct = 0
stud_disct = 0
weeknd_chrg = 0
vip_charge = 0

if (age > 0 and age < 15):
    child_disct = 0.1 * base
    stud_disct = 0 

elif student == "y" or student == "Y":
    stud_disct = 0.15 * base
    child_disct = 0  

else:
    child_disct = 0
    stud_disct = 0


if(weekend == "y" or weekend =="Y"):
    weeknd_chrg = 100
else:
    weeknd_chrg = 0

if(VIP == "y" or VIP =="Y"):
    vip_charge = 250
else:
    vip_charge = 0

total = 0
total = base + weeknd_chrg + vip_charge
total = total - child_disct - stud_disct

print("the total ticket price is ₹",total)
    