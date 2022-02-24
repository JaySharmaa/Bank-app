from datetime import datetime,date
from colorama import Fore, Style
import time

today = date.today()

class Bank:
    def __init__(self,existing_amount=0):
        self.current= existing_amount    
    
    def Transactionlog(self,transaction_log):
        with open("Transaction.txt", "a") as file:
            file.write(f"{transaction_log}")
    
    def withdraw(self):
        _now = datetime.now()
        with_amount = input("Enter The Amount to Withdraw : ")
        try:
            with_amount = float(with_amount)
            if self.current<with_amount:
                time.sleep(0.5)
                print(Fore.RED+Style.BRIGHT+"\nBalance Low !!")
                print(Style.RESET_ALL)

            elif self.current>=with_amount:
                self.current = self.current - with_amount
                time.sleep(0.3)
                print("\nProcessing.............\n")
                time.sleep(1)
                print(Fore.GREEN+Style.BRIGHT+"Succesful !!")
                print(Style.RESET_ALL)
                time.sleep(0.5)
                print(Fore.BLUE+Style.BRIGHT+"Current Balance : ",self.current,"\n")
                self.Transactionlog(f"\n({today}) \nWithdraw : {with_amount}\nCurrent balance : {self.current}\nTime : {_now.strftime('%H:%M:%S')}\n")
            else:
                print("Some Error Occuring Please Try Again !!\n")
        except ValueError:
            print("Wrong Value !!")

        
    
    def deposit(self):
        _now = datetime.now()
        depo_amount = input("Enter The Amount to Deposit : ")
        try:
            depo_amount = float(depo_amount)
            if depo_amount:
                self.current = self.current + depo_amount
                time.sleep(0.3)
                print("\nProcessing.............\n")
                time.sleep(1)
                print(Fore.GREEN+Style.BRIGHT+"Succesful !!")
                print(Style.RESET_ALL)
                time.sleep(0.5)
                print(Fore.BLUE+Style.BRIGHT+"Current Balance : ",self.current,"\n")
                print(Style.RESET_ALL)   
                time.sleep(0.5)
                self.Transactionlog(f"\n({today}) \nDeposit : {depo_amount}\nCurrent balance : {self.current}\nTime : {_now.strftime('%H:%M:%S')}\n")
            else:
                print("Some Error Occuring Please Try Again !!")

        except ValueError:
            time.sleep(0.5)
            print("Wrong Value !!")
    
    def Current(self):
        time.sleep(0.5)
        print(Fore.CYAN+Style.BRIGHT+"Current Balance IS : ",self.current,"\n")
        print(Style.RESET_ALL)
        time.sleep(0.5)

bank = Bank()

print(Fore.MAGENTA+Style.BRIGHT+"\n\t\t##### Welcome To The Bank #####\n")
Exit=False
while Exit==False:
    choice = input(Fore.WHITE + Style.BRIGHT + "What would you like to Do ??\n0. Withdraw\n1. Deposit\n2. Current Balance\n3. Exit\n --> ").lower()
    print(Style.RESET_ALL)
    if choice in ['0','1','2','3','exit','withdraw','deposit','current']:

        if choice=='0' or choice=='withdraw':
            bank.withdraw()
            
        
        elif choice=='1' or choice=='deposit':
            bank.deposit()

        elif choice=='2' or choice=='current':
            bank.Current()

        elif choice=='3' or choice=='exit':
            time.sleep(0.3)
            print(Fore.LIGHTYELLOW_EX+Style.BRIGHT+"Thank u for visiting !!")
            print(Style.RESET_ALL)
            time.sleep(0.5)
            Exit=True
        else:
            time.sleep(0.5)
            print('Wrong Input !!\n')

    else:
        time.sleep(0.5)
        print("Wrong Input !!\n")