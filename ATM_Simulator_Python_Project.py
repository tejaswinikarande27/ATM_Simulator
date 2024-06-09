#!/usr/bin/env python
# coding: utf-8

# In[4]:


class User:
    def __init__(self, pin, balance, name):
        self.balance = balance
        self.correct_pin = pin
        self.name = name
def atm_simulation(user):
    balance=10000
    print(f'''
            ***** Welcome {user.name} To ATM Machine Simulator *****
         ''')

    pin=int(input('Enter Your Pin: '))
    if pin!=user.correct_pin:
      print("Incorrect pin")
      print("Thank you")
      return
    while True:
      print('''
              Options you can Excercise are:
              1) Balance
              2) Withdraw
              3) Deposit
              4) Change pin
              5) Exit
          ''')
      choose=int(input('Select Your Transaction from the above options: '))
      if choose==1:
          print(f'Available A/C Balance Is {user.balance}')
      elif choose==2:
          withdraw=int(input('Enter Amount: '))
          if withdraw<=user.balance:
              user.balance-=withdraw
              print(f'Your availabe balance is {user.balance}')
          else:
              print('Insufficient Balance')
      elif choose==3:
          amount=int(input('Enter Amount: '))
          user.balance+=amount
          print(f'New Balance is {user.balance}')
      elif choose==4:
          new_pin = int(input("Enter the new pin: "))
          user.correct_pin = new_pin
      elif choose==5:
          print("Thank you!")
          break
      else:
          print('Incorrect choice')
    return


# In[6]:


Tejaswini = User(2345, 100000, "Tejaswini")


# In[7]:


atm_simulation(Tejaswini)


# In[17]:


Tejaswini= User(1277, 15000,"Tejaswini")


# In[18]:


atm_simulation(Tejaswini)

