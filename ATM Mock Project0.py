name = input("Welcome, What is your name? \n")
allowedUsers = ['Oba', 'Eniola', 'Grace']
allowedPassword = ['passOba', 'passEni', 'passG']
import datetime
date = datetime.datetime.now()

if(name in allowedUsers):
    password = input("Your Password? \n")
    userId = allowedUsers.index(name)

    if(password == allowedPassword[userId]):

        print('Welcome %s' %name)
        print('Current Date and Time: %s' %date.strftime('%c'))
        print('What action would like to perform today? Select from options 1 to 3')
        print('1. Withdrawal')
        print('2. Cash Deposit')
        print('3. Complaint')

        selectedOption = int(input('Please select an option:'))

        if(selectedOption == 1):
            amount = input("How much would like to Withdraw? \n")
            print("Take Your Cash")

        elif(selectedOption == 2):
            deposit = input("How much would you like to deposit? \n")
            print("Your current balance is %s" %deposit)

        elif(selectedOption == 3):
            Complaint = input("What issue will you like to report? \n")
            print("Thank you for contacting us")

        else:
            print('Invalid Option selected, please try again')

    else:
        print('Password Incorrect, Please try again')

else:
    print('Name not found, please try again')
        
