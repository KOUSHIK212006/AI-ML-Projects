password=input("\nenter your password\n")

upper=False
lower=False
digit=False
special=False

special_character="~!@#$%^&*()_+{}:<>?-=[];',./|"

for char in password:
    if char.isupper():
        upper=True
    elif char.islower():
        lower=True
    elif char.isdigit():
        digit=True
    elif char in special_character:
        special=True

score=0

if len(password)>=8:
    score+=1
if upper:
    score+=1
if lower:
    score+=1
if digit:
    score+=1
if special:
    score+=1

if score<=2:
    print("\nPassword Strength: Weak")
elif score==3 or score ==4:
    print("\nPassword Strength: Medium")
else:
    print("\nPassword Strength: Strong")
