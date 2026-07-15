import random
import json
import os


print("\n\n.................Welcome to.. Private bank of GPT....................\n")

def check_balance(account):
    print(f"\nAvailbale Balance\n\n ₹{accounts[account]['balance']}")
    print("\nThenk you for banking with us😊\n")
    

def Deposite_balance(account):
    amount = int(input("Enter amount to deposite :"))
    if amount <= 0:
        print("Invalid amount.") 
        return
    accounts[account]['balance'] += amount
    accounts[account]["history"].append(f"Deposit : +₹{amount}")
    
    with open("Python_Projects/accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    print("\nAmount deposite successfull..\n")
    
    
def Withdraw_balance(account):
    amount = int(input("Enter amount to withdraw : "))
    if amount >= accounts[account]['balance']:
        print("\nInsufficient Balance.\n")
        return
    accounts[account]['balance'] -= amount
    accounts[account]["history"].append(f"Withdraw : -₹{amount}")

    with open ("Python_Projects/accounts.json","w") as file:
        json.dump(accounts, file , indent=4)
    print(f"\nAmount ₹{amount} withdrawn successfully...\n.")
    

def Change_pin(account):
    old_pin = int(input("Enter old pin.. :"))
    if accounts[account]['pin'] != old_pin:
        print("\nIncorrect pin.\n")
        return
    newPin = input("Enter new pin.. : ")
    if len(newPin) != 4 or not newPin.isdigit():
        print("\nPin must be exacty 4 digits \n")
        return
    accounts[account]['pin'] = int(newPin)
    
    with open("Python_Projects/accounts.json", "w") as file:
        json.dump(accounts, file, indent=4)
    
    print("\nPIN changed successfully.\n")
    
    
def delete_ac(account):
    del accounts[account]
    print(f"\nAccount {account} deleted successfully\n")
    
    with open("Python_Projects/accounts.json","w")as file:
        json.dump(accounts,file,indent=4)
    
    

def Statement(account):
    print("\n--------------Mini Statement-------------\n")
    print(f"Holder Name : {accounts[account]['name']}")
    print(f"Account Number : {account}")
    print(f"Available Balance : ₹{accounts[account]['balance']}")
    print("\nRecent Transaction")
    for transaction in accounts[account]['history'][-5:]:
        print(transaction)
    print("---------------------------------------------\n")


try:
    with open("Python_Projects/accounts.json","r") as file:
        accounts = json.load(file)
    accounts = {int(k): v for k, v in accounts.items()}

except FileNotFoundError:
    accounts={}

while True:
    print("____________Main manu______________\n")
    print("1- Login existing Account")
    print("2- Open an Account")
    print("3- Exit")
    
    try:
        value = int(input("Enter your choice :"))
    except ValueError:
            print("\nInvalid input \n")
            continue
    
    if value == 1:
        AC_number = int(input('Enter Your Account Number : '))
        if AC_number in accounts:
            attempt = 3
            while attempt > 0:
                pin = int(input("Enter your pin..: "))     
                if pin == accounts[AC_number]['pin']:
                    print("\nYou are Successfully logged in..\n")
                    break
                attempt -=1
                print(f"Wrong pin !! you have only {attempt} left\n")

            if attempt == 0:
                print("\nMaximum attemp left\n")
                continue
                       
            while True:
                print('1- Check Balance')
                print('2- Deposite')
                print('3- Withdraw')
                print('4- Change pin')
                print('5- Mini Statement')
                print("6- Delete account")
                print('7- Logout')
                num = int(input("Please tell me what you want.. :"))
                if num == 1 :
                     check_balance(AC_number)
                elif num == 2:
                    Deposite_balance(AC_number)
                elif num == 3:
                     Withdraw_balance(AC_number)
                elif num == 4 :
                    Change_pin(AC_number)
                elif num == 5:
                    Statement(AC_number)
                elif num == 6:
                    delete_ac(AC_number)
                    break
                elif num == 7:
                    print("\nLogged Out")
                    break
        else:
            print('\nInvalid account number\n')    
            
        
    elif value == 2:
        saved_name = input("Enter name..: ")
        while True:
            saved_account = random.randint(100000,999999)
            if saved_account not in accounts:
                break
            
        print(f'Your generated account number :{saved_account}')
        
        while True:
            saved_pin = input("Make your pin (4 digit pin..) : ")
            if len(saved_pin) == 4 and saved_pin.isdigit():
                saved_pin = int(saved_pin)
                break
            print("PIN must be exactly 4 digits.")
            
                
        saved_balance = int(input('Deposite some initial amount : '))
        print('\nAccount Successfully created....')
        
        accounts[saved_account] = {
            'name':saved_name,
            'pin':saved_pin,
            'balance':saved_balance,
            'history':[]
        }
        with open("Python_Projects/accounts.json", "w") as file:
            json.dump(accounts, file, indent=4)
        
    elif value == 3:
        print('\nThank you\n')
        break