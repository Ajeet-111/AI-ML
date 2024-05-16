name=input("Enter your name: ")
print("WElcome!,", name, '\n')

print(f"How may i help you sir?")

choice="""
Choose one of these options: 
Type 1 --> Check balance.
Type 2 --> Deposit money.
Type 3 --> Withdraw money.
"""
print(choice)
task=int(input("Enter your task: "))

if task >=1 and task <= 3:
    balance= 1200
    if task==1:
        pin=int(input("enter your pin: "))        
        if pin==0000:
            print("Mr."+name+", your available balance is $",balance)
        else:
            print("Incorrect pin.")

# deposite
    elif task==2:
        amount=int(input("Enter amount: $"))
        pin=int(input("enter your pin: "))
        print()
        if pin==0000:
            if amount>=500:
                balance+=amount
                print("Mr."+name+", you have succefully deposited $",amount,"in your account.")
                print("Now, Your available balance is: $",balance)
            else:
                print("please enter more than $500")                        
        else:
            print("Incorrect pin.")

# withdraw
    elif task==3:
        amount=int(input("Enter amount: $"))
        pin=int(input("enter your pin: "))
        print()
        if pin==0000:
            if amount<=balance:
                balance-=amount
                print("Mr."+name+" you have succefully withdrawn $",amount,"from your account.")
                print("Now, Your available balance is $",balance)
            else:
                print("please enter a valid amount.")                        
        else:
            print("Incorrect pin.")
else:
    print("Choose a valid option!")