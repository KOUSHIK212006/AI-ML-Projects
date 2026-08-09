account={
    "name":"Thomas",
    "balance":10000
}
transactions=[]

def deposit():
    amount=float(input("enter the amount to be deposited:\n"))
    if amount<=0:
        print("invalid amount")
        return
    else:
        account["balance"]+=amount

    transaction={
        "type":"deposit",
        "amount":amount,
        "balance_after":account["balance"]
    }
    transactions.append(transaction)
    print("Deposited Successfully")
    print("current balance: ",account["balance"])

def withdraw():
    amount=float(input("enter amount to withdraw:\n"))
    if amount<=0:
        print("invalid amount")
        return
    if amount>account["balance"]:
        print("Insufficient balance")
    account["balance"]-=amount
    transaction={
        "type":"withdraw",
        "amount":amount,
        "balance_after":account["balance"]
    }
    transactions.append(transaction)
    print("Withdrawn Successfully")
    print("current balance: ",account["balance"])

def check_balance():
    print("Balance:",account["balance"])

def account_details():
    print("~~~~~~ACCOUNT DETAILS~~~~~~~~~~")
    print("ACCOUNT HOLDER NAME: ",account["name"])
    print("BALANCE: ",account["balance"])
    print("NO OF TRANSACTIONS: ",len(transactions))

def main():
    while True:
        print("1.DEPOSIT")
        print("2.WITHDRAW")
        print("3.CHECK BALANCE")
        print("4.ACCOUNT DETAILS")
        print("5.TRANSACTION HISTORY")
        print("6.EXIT")
        choice=int(input("enter your choice:\n"))
        if choice==1:
            deposit()
        elif choice==2:
            withdraw()
        elif choice==3:
            check_balance()
        elif choice==4:
            account_details()
        elif choice==5:
            if len(transactions)==0:
                print("No Transactions")
            else:
                for x in transactions:
                    print("Type:",x["type"])
                    print("Amount:",x["amount"])
                    print("Balance Afetr:",x["balance_after"])
        elif choice==6:
            print("Thank You")
            break
        else:
            print("invalid choice")

main()
