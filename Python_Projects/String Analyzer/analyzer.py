stri = input("Enter the string : ")
stri = stri.lower() 
total_chr = len(stri) #To Count total characters
words = len(stri.split()) #To Count words

#To count Vowels and consonants : 
vowels = 0
consonants = 0

for i in stri:
    if i in "aeiou":
        vowels+=1
    elif i.isalpha():
        consonants+=1

#To Count digits:
digits = 0
for i in stri:
    if i.isdigit():
        digits+= 1 

# To Count spaces:
space = 0
for i in stri:
    if i.isspace():
        space+=1

#To Count special characters
special = 0
for i in stri:
    if not i.isalnum() and not i.isspace():
        special += 1

# To Display the reversed string:
rev = stri[::-1]

#To Check if the sentence is a palindrome:
palind = True
state = ""

if rev == stri :
    palind = True
else:
    palind = False

if palind:
    state = "YES"
else:
    state = "NO"

#Displaying Output:
print("Characters :", total_chr)
print("Words :",words)
print("Vowels :",vowels)
print("Consonants :",consonants)
print("Digits :",digits)
print("Spaces :",space)
print("Special :",special)
print("Reversed :",rev)
print("Palindrome :",state)