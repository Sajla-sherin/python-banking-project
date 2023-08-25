from bank import chkbalance

acountNO = 0
cusName = ""
mobile = 0
Bcode = ""
Bal = 0

def acounts():
    global acountNO, cusName, mobile, Bcode, Bal

def createacounts():
    global acountNO, cusName, mobile, Bcode, Bal
    acountNO = int(input("enter account number"))
    cusName = input("enter name")
    Bcode = int(input("enter branch code "))
    mobile = int(input("enter mobile number"))
    Bal = int(input("enter current balance"))

def showAcountDetails():
    print("acountNO:", acountNO)
    print("customerName:", cusName)
    print("Bcode", Bcode)
    print("mobile:", mobile)

def deposit(amount):
    global Bal
    Bal = Bal + amount
    chkbalance()

def withdraw(amount):
    global Bal
    Bal = Bal - amount
    chkbalance()

def chckbalance():
    print("current balance:", Bal)

# _main_
print("1.create account  \n 2.withdraw \n 3.deposit \n 4.check balance")
ch = int(input("select any option"))
if ch == 1:
    createacounts()
elif ch == 2:
    amnt = int(input("enter amount to withdraw"))
    withdraw(amnt)
elif ch == 3:
    amnt = int(input("enter amount to deposit"))
    deposit(amnt)
elif ch == 4:
    chckbalance()
else:
    print("please select any 4 options available above")
    print("do you want to contenue....press y")


