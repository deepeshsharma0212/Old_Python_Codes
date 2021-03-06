import time
import getpass
import sqlite3 as sql

db = sql.connect('bank.db')
c = db.cursor()



def credit(name):

    amount = int(input("\n\nEnter amount to deposit = "))
    c.execute('select * from bank where user="%s"'%name)
    data = c.fetchall()
    l = list(data[0])
    l[3] += amount
    c.execute('update bank set bal=%i where user="%s"'%(l[3],name))
    time.sleep(2)
    print("\nYou have sucessfully credited bal %s rs in your account"%(amount))
    print("\n\nUpdated Balance = %s"%(l[3]))
    choice(name)

def debit(name):
    c.execute('select bal from bank where user="%s"'%(name))
    bal = c.fetchall()
    bal = bal[0][0]
    amount = int(input("\n\nEnter amount to withdraw = "))
    if bal > amount :
        bal -= amount
        c.execute('update bank set bal=%i where user="%s"'%(bal,name))
        db.commit()
        time.sleep(2)
        print("\nYou have sucessfully debited bal %s rs in your account"%(amount))
        print("\n\nUpdated Balance = %s"%(bal))
        choice(name)
    else :

        print("\n\nYou does not have suffcient balance in your account \n\nTry Again \n\n")
        time.sleep(2)
        debit(name)

def chk_bal(name):

        c.execute("select * from bank where user='%s'"%(name))
        data = list(c.fetchall()[0])
        print("Name = ",data[0])
        print("Account Number = ",data[1])
        print("Your Balance = %s rupees "%(data[3]))
        choice(name)
    




def choice(name):
    
    print("\n\n1.Debit\n2.Credit\n3.Chk_balance\n4.Profile\n5.logout\nEnter your choice - ",end='')
    ch = int(input())
    if ch == 1 :

        debit(name)

    elif ch == 2 :

        credit(name)

    elif ch == 3 :

        chk_bal(name)

    elif  ch == 4 :

        profile(name)

    elif ch == 5 :

        print("\n\nThanks for using python bank \n\n")
        time.sleep(3)
        main()
    else :

        print("\n\nInvalid choice \n\nTry Again \n\n")
        time.sleep(3)
        choice(name)






def sign_up():

    name = input("Enter your name - ").strip()
    c.execute('select user from bank')
    data = c.fetchall()
    bank = []
    for d in data :
       bank.append(d[0])

    if name.lower() in bank :

        print("User name already taken \nChoose another name ")
        sign_up()
    else:

        pass1=getpass.getpass()
        pass2=getpass.getpass("Confirm Password :")

        if pass1 == pass2 :

            bal = int(input("\nEnter amount to credit - "))
            c.execute('select acc_no from bank')
            all_acc = c.fetchall()
            bank = []
            for var in all_acc :
                bank.append(var[0])
            acc_no = bank[-1]+1
            c.execute('insert into bank(user,acc_no,password,bal) values(\'{}\',{},\'{}\',{})'.format(name,acc_no,pass1,bal))
            db.commit()
            
            login()

        else:
            print("\n\nPassword Does not Match...Try again\n\n")
            time.sleep(3)
            sign_up()


def login():
    
    print("\n\nWelcome to Login facility \n\n")
    c.execute('select user from bank')
    data = c.fetchall()
    bank = []
    for d in data :
       bank.append(d[0])

    name = input("Enter your user name - ").strip()
    if name.lower() in bank:
        password = getpass.getpass()
        c.execute('select password from bank where user="%s"'%(name))
        data = c.fetchall()
        if password == data[0][0] : 

            choice(name)
        else :
            login()
    else :

        print("Wrong input press y to continue ")
        ch = input().strip()

        if ch.lower() == 'y':

            login()
        else :

            print("\n\nThanks for using python bank \n\n")
            time.sleep(3)
            exit(0)



def main():

    print("\n\nWelcome to python Bank \n\n")
    ch = int(input("1.login\n2.sign_up\n3.exit\nEnter your choice - "))
    if ch == 1 :

        login()
    elif ch == 2 :

        sign_up()
    elif ch == 3 :

        print("\n\nThanks for using python bank \n\n ")
        time.sleep(3)
        exit(0)
    else :
        print("Wrong Choice Try again ")
        main()


if __name__ == '__main__' :

    main()
