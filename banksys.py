# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 14:58:48 2024

@author: ankit
"""
class BankSystem:
    def __init__(self,account_no,account_holder,balance):
        self.account_no=account_no
        self.account_holder=account_holder
        self.balance=balance   
    def check_balance(self):
        print("Account No: {} | Account Holder: {} | Available Balance:{}".format(self.account_no,self.account_holder,self.balance))
    def withdraw_amount(self,amount):
        if amount<self.balance:
            self.balance -=amount
            print(f"{amount} has been withdrawn")
        else:
            print("Insufficient Balnce")
    def credit_amount(self,amount):
        self.balance+=amount
        print(f"{amount} has been credited successfully")
        pass
    def update_account_holder(self,new_holder):
        self.account_holder=new_holder
        print(f"{new_holder} has been updated")
    
c1=BankSystem(222,"Ankit", 500)
while True:
    n=input("Press 1.check balance| 2.withdraw amount | 3.credit amount | 4.update holder \ 5.exit")
    if n==1:
        c1.check_balance()
    elif n==2:
        amount=int(input("Enter amount to withdraw"))
        c1.withdraw_amount(amount)
        c1.check_balance()
    elif n==3:
        amount=int(input("Enter amount to withdraw"))
        c1.credit_amount(amount)
        c1.check_balance()
    elif n==4:
        new_holder=input("Enter new holder name to update")
        c1.update_account_holder(new_holder)
    else:
        print("Exiting")
c1.withdraw_amount(300)
c1.check_balance()
c1.credit_amount(1000)
c1.check_balance()
c1.update_account_holder("Alan")