pin = int(input("Set the PIN: "))
attempts = 3

while attempts > 0:
    pin1 = int(input("Enter the PIN: "))

    if pin == pin1:
        print("Verification Successful")
        print("Welcome!")
        break
    else:
        attempts -= 1

        if attempts > 0:
            print("Verification Failed.")
            print(attempts, "attempt(s) left")
        else:
            print("Account Locked after 3 failed attempts.")
