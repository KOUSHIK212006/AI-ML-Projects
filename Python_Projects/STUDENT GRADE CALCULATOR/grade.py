name=input("\nEnter your name:")
print("\nEnter the marks obtained by the student out of 100\n")

sub1=float(input("\nSubject 1:"))
sub2=float(input("\nSubject 2:"))
sub3=float(input("\nSubject 3:"))
sub4=float(input("\nSubject 4:"))
sub5=float(input("\nSubject 5:"))

total=sub1+sub2+sub3+sub4+sub5

percentage=(total/500)*100

highest=max(sub1,sub2,sub3,sub4,sub5)

lowest=min(sub1,sub2,sub3,sub4,sub5)

if percentage>=90:
    grade="A+"
elif percentage>=80 and percentage<90:
    grade="A"
elif percentage>=70 and percentage<80:
    grade="B"
elif percentage>=60 and percentage<70:
    grade="C"
elif percentage>=50 and percentage<60:
    grade="D"
else:
    grade="F"

if sub1>=35 and sub2>=35 and sub3>=35 and sub4>=35 and sub5>=35:
    result="PASS"
else:
    result="FAIL"

print("\n~~~~~~~~~~~STUDENT REPORT CARD~~~~~~~~~~~~~~~\n")
print("\nSTUDENT NAME: ",name)
print("\nTOTAL MARKS: ",total)
print("\nPERCENTAGE: ",percentage)
print("\nGRADE: ",grade)
print("\nRESULT: ",result)
print("\nHIGHEST: ",highest)
print("\nLOWEST: ",lowest)