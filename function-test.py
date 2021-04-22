import random

database = {}

def init():
    optionSelected = False

    print("Welcome, what would you like to do?")
    print("1. Login")
    print("2. Register")

    actionSelect = input('Select an option \n')

    if(actionSelect == '1'):
        optionSelected == True
        login()

    elif(actionSelect == '2'):
        optionSelected == True
        register()
                
    else:
        print('Wrong option')
        init()

def generateAccountNumber():
    return random.randrange(0000000000, 9999999999)

def register():
    firstname = input('What is your first name? \n')
    lastname = input('What is your last name? \n')
    password = input('Enter a password? \n')

    accountNumber = generateAccountNumber()

    print('Generating account number...')
    print('Acount has been created')
    print('Dear %s %s your account number is %d ' % (firstname, lastname, accountNumber))

    database[accountNumber] = [firstname, lastname, password, {'balance' : 0}]
    login()

def login():
    print('log into your account')
    
    userAccountNumber = int(input('Enter your account Number \n'))
    userPassword = input('Enter your password \n')

    x = False

    for accountNumber, userDetails in database.items():
        if(accountNumber == userAccountNumber):
            if(userDetails[2] == userPassword):
                while x == False:
                    bankOperations(userDetails)
        print('invalid login details')

def bankOperations(user):
    print('******** log in successful ********')
    print('Welcome back %s %s' % (user[0], user[1]) )

    option = input('What would you like to do today? [1] deposit [2] Withdraw [3] Balance [4] Transfer [5] logout \n')

    if(option == '1'):
        deposit(user)
    elif(option == '2'):
        withdraw(user)
    elif(option == '3'):
        balance(user)
    elif(option == '4'):
        transfer(user)
    elif(option == '5'):
        logout()
    else:
        print('Wrong option selected \n')
        bankOperations(user)

def deposit(user):
    amount = int(input('How much would you like to deposit? \n'))

    if (amount > 0):
        user[3]['balance'] += amount
        print('You have successfully deposited %d ' % (amount))
    else:
        print('Invalid amount')

def withdraw(user):
    amount = int(input('How much would you like to Withdraw? \n'))
    if (amount > user[3]['balance']):
        print('insufficient balance')
    else:
        user[3]['balance'] -= amount
        print('*** Take your %d ***' % amount)

def balance(user):
    print('Your current account balance is %d ' %(user[3]['balance']))

def transfer(user):
    aza = int(input('Enter the account number of the receipent \n'))

    if(aza in database.keys()):
        receipent = database[aza]
        amount = int(input('Enter amount \n'))
        if (amount <= user[3]['balance']):
            user[3]['balance'] -= amount
            receipent[3]['balance'] += amount
            print('%d has been transferred successfully to %s %s ' % (amount, receipent[0], receipent[1]))
        else:
            print('insufficient balance')
    else:
        print('Wrong account number try again \n')


def logout():
    init()

init()