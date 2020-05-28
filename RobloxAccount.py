from time import sleep
def password():
    tries = 0
    while tries < 3:
        pin = int(input("Please enter your pin in the screen "))
        if pin == (1234):
            print("Correct..fetching your data in a few seconds...")
            return True
        else:
            print("Incorrect password, please try again")
            tries = tries + 1
    print("Incorrect password, and system is self-destructing for attempts in 3 seconds")
    sleep(3)
    return False


def start():
    balance = 500

    print("Hello, and welcome to your virtual ROBUX ATM")
    if password():
        print("1: for Balance")
        print("2: for Withdrawal")
        print("3: for Deposit")
        print("4 for Exit")

        transaction = int(input("Choose which robux transaction fits your day: "))
        if transaction == 1:
            print("Your balance is R$",balance,'\n')
            restart = input("would you like to go back? ")
            if restart in('No','no'):
                print("Thanks for using ROBUX ATM. Bye!")
            elif restart in('Yes','y'):
                print("")
                start()

        elif transaction == 2:
            withdrawal = float(input("How much would you like to withdraw?\nR$80\nR$400\nR$800\nR$1000\nR$10000\nR$20000"))
            if withdrawal in [80,400,800,100,10000,20000]:
                balance = balance - withdrawal
                print("Your balance is: ", balance)
                restart = input("Would you like to go back? ")
                if restart in('No', 'no'):
                    print("Thanks for using ROBUX ATM. Bye!")
                elif restart in('Yes','y'):
                    print("")
                    start()
            elif withdrawal != [80,400,800,100,10000,20000]:
                print("Invalid Amount, try again.")
                restart = ('yes')


        elif transaction == 3:
            deposit = float(input("How much robux do you want to deposit? "))
            balance = deposit + balance
            print("Your balance is R$:", balance, '\n')
            restart = input("Woud you like to go back? ")
            if restart in ('No', 'no'):
                print('Thanks for using ROBUX ATM. Bye!')
            elif restart in ('Yes', 'y'):
                print("")
                start()

        elif transaction == 4:
            print("Thanks for using ROBUX ATM, hope you have a great day for you ahead.")
            print("Exiting program....")

start()
