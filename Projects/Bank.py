
account_order = 0
####################
####################


def enter_account_details(number):
    global account_order
    account_order += 1
    if number == 1:
        first_name = input("Please enter client's first name :")
        while not first_name.isalpha():
            first_name = input("please re-enter the name correctly :")

        last_name = input("Please enter client's last name :")
        while not last_name.isalpha():
            last_name = input("please re-enter the name correctly :")
        full_name = (first_name+" "+last_name).title()
        phone_number = input("Please enter client's phone number :")
        while (not phone_number.isnumeric()) or (len(phone_number) < 8):
            phone_number = input(
                "please enter a valid number that is not less than 8 digits :")
        phone_number = int(phone_number)
        while True:
            try:
                balance = float(input("please enter client's balance :"))
                while balance < 1000:
                    balance = float(input(
                        "a client's balance should contain 1000 L.E as a minimum, please re-enter the balance :"))
            except ValueError:
                print("A balance cannot contain letters !")
            else:
                break
        all_client_info = dict(client_account_type="Basic Account", account_number=account_order,
                               client_name=full_name, client_balance=balance, client_phone_number=phone_number)
        all_accounts.append(all_client_info)
        print("A Basic account was created successfully !")
        print("*"*30)
        print("Account type : {}".format(
            all_client_info["client_account_type"]))
        print("Account number : {}".format(all_client_info["account_number"]))
        print("Client name : {}".format(all_client_info["client_name"]))
        print("Balance : {} L.E".format(all_client_info["client_balance"]))
        print("Client phone number : {}".format(
            all_client_info["client_phone_number"]))
        print("*"*30)

    if number == 2:
        first_name = input("Please enter client's first name :")
        while not first_name.isalpha():
            first_name = input("please re-enter the name correctly :")

        last_name = input("Please enter client's last name :")
        while not last_name.isalpha():
            last_name = input("please re-enter the name correctly :")
        full_name = (first_name+" "+last_name).title()
        phone_number = input("Please enter client's phone number :")
        while (not phone_number.isnumeric()) or (len(phone_number) < 8):
            phone_number = input(
                "please enter a valid number that is not less than 8 digits :")
        phone_number = int(phone_number)
        while True:
            try:
                balance = float(input("please enter client's balance :"))
                while balance < 100000:
                    balance = float(input(
                        "a client's V.I.P account balance should contain 100000 L.E as a minimum, please re-enter the balance :"))
            except ValueError:
                print("A balance cannot contain letters !")
            else:
                break
        all_client_info = dict(client_account_type="V.I.P Account", account_number=account_order,
                               client_name=full_name, client_balance=balance, client_phone_number=phone_number)
        all_accounts.append(all_client_info)
        print("A V.I.P account was created successfully !")
        print("*"*30)
        print("Account type : {}".format(
            all_client_info["client_account_type"]))
        print("Account number : {}".format(all_client_info["account_number"]))
        print("Client name : {}".format(all_client_info["client_name"]))
        print("Balance : {} L.E".format(all_client_info["client_balance"]))
        print("Client phone number : {}".format(
            all_client_info["client_phone_number"]))
        print("*"*30)


####################
####################
all_accounts = []
lets_roll = "1"
while lets_roll == "1":
    print("*"*20)
    print("Welcome To The Bank Homie:\nWhat Do You Wanna Do ?\n"
          "Press 1 to add a new client\nPress 2 to show clients and their accounts\n"
          "Press 3 to deposit\nPress 4 to withdraw\nPress 5 to delete an account")
    print("*"*20)
####################
    while True:
        try:
            navigator = int(input("please enter a number :"))
            while not(navigator == 1 or navigator == 2 or navigator == 3 or navigator == 4 or navigator == 5):
                navigator = int(input("please enter a number from 1 to 5 :"))
        except ValueError:
            print("Please enter the right number !")
        else:
            break
####################
    if navigator == 1:
        while True:
            try:
                account_type = int(
                    input("for basic account press 1, for V.I.P account press 2 :"))
                while not(account_type == 1 or account_type == 2):
                    account_type = int(input("please enter either 1 or 2 :"))
            except ValueError:
                print("Please enter the right number !")
            else:
                break
        enter_account_details(account_type)
####################
    if navigator == 2:
        if not all_accounts:
            print("there are currently no accounts to be shown, please enter at least one account then come back again")
        else:
            for acc in all_accounts:
                print("*"*30)
                print("Account type : {}".format(acc["client_account_type"]))
                print("Account number : {}".format(acc["account_number"]))
                print("Client name : {}".format(acc["client_name"]))
                print("Balance : {} L.E".format(acc["client_balance"]))
                print("Client phone number : {}".format(
                    acc["client_phone_number"]))
                print("*"*30)
####################
    if navigator == 3:
        if not all_accounts:
            print(
                "there are currently no accounts, please enter at least one account then come back again")
        else:
            finder = input(
                "Please enter the account number for the account that you want to deposit in :")
            while not finder.isdigit():
                finder = input("Please enter a number :")
            finder = int(finder)
            for acc in all_accounts:
                if acc["account_number"] == finder:
                    print(
                        f"An account with Account number {finder} was found, and here are its details")
                    print("*"*30)
                    print("Account type : {}".format(
                        acc["client_account_type"]))
                    print("Account number : {}".format(acc["account_number"]))
                    print("Client name : {}".format(acc["client_name"]))
                    print("Balance : {} L.E".format(acc["client_balance"]))
                    print("Client phone number : {}".format(
                        acc["client_phone_number"]))
                    print("*"*30)
                    while True:
                        try:
                            depositer = float(
                                input("Please enter the amount of money you want to deposit :"))
                        except ValueError:
                            print("please enter a valid number !")
                        else:
                            break
                    acc["client_balance"] += depositer
                    print(
                        f"An amount of {depositer} L.E was deposited successfully")
                    print("*"*30)
                    print("Account type : {}".format(
                        acc["client_account_type"]))
                    print("Account number : {}".format(acc["account_number"]))
                    print("Client name : {}".format(acc["client_name"]))
                    print("Balance : {} L.E".format(acc["client_balance"]))
                    print("Client phone number : {}".format(
                        acc["client_phone_number"]))
                    print("*"*30)
                    break
            else:
                print(
                    "No such account with the account number you entered was found")
####################
    if navigator == 4:
        if not all_accounts:
            print(
                "there are currently no accounts, please enter at least one account then come back again")
        else:
            finder = input(
                "Please enter the account number for the account that you want to withdraw from :")
            while not finder.isdigit():
                finder = input("Please enter a number :")
            finder = int(finder)
            for acc in all_accounts:
                if acc["account_number"] == finder:
                    print(
                        f"An account with Account number {finder} was found, and here are its details")
                    print("*"*30)
                    print("Account type : {}".format(
                        acc["client_account_type"]))
                    print("Account number : {}".format(acc["account_number"]))
                    print("Client name : {}".format(acc["client_name"]))
                    print("Balance : {} L.E".format(acc["client_balance"]))
                    print("Client phone number : {}".format(
                        acc["client_phone_number"]))
                    print("*"*30)
                    while True:
                        try:
                            withdrawl = float(
                                input("Please enter the amount of money you want to withdraw :"))
                            while withdrawl > acc["client_balance"]:
                                withdrawl = float(input(
                                    "you can't withdraw an amount greater than the balance, please re-enter the amount you want to withdraw :"))
                        except ValueError:
                            print("please enter a valid number !")
                        else:
                            break
                    acc["client_balance"] -= withdrawl
                    print(
                        f"An amount of {withdrawl} L.E was withdrawn successfully")
                    print("*"*30)
                    print("Account type : {}".format(
                        acc["client_account_type"]))
                    print("Account number : {}".format(acc["account_number"]))
                    print("Client name : {}".format(acc["client_name"]))
                    print("Balance : {} L.E".format(acc["client_balance"]))
                    print("Client phone number : {}".format(
                        acc["client_phone_number"]))
                    print("*"*30)
                    break
            else:
                print(
                    "No such account with the account number you entered was found")
####################
    if navigator == 5:
        if not all_accounts:
            print("there are currently no accounts to delete from")
        else:
            finder = input(
                "Please enter the account number for the account you want to delete :")
            while not finder.isdigit():
                finder = input("Please enter a number :")
            finder = int(finder)
            for acc in all_accounts:
                if acc["account_number"] == finder:
                    print(
                        f"An account with Account number {finder} was found, and here are its details")
                    print("*"*30)
                    print("Account type : {}".format(
                        acc["client_account_type"]))
                    print("Account number : {}".format(acc["account_number"]))
                    print("Client name : {}".format(acc["client_name"]))
                    print("Balance : {} L.E".format(acc["client_balance"]))
                    print("Client phone number : {}".format(
                        acc["client_phone_number"]))
                    print("*"*30)
                    it_is_over = input("Are you sure you want to delete that cute innocent account ?"
                                       "\nif so type \"yes\", typing otherwise will keep that bae :")
                    if it_is_over.lower() == "yes":
                        all_accounts.remove(acc)
                        print(
                            "Account was deleted successfully, hope you are having fun")
                        break
                    else:
                        print(
                            "Account was not deleted since you discarded the operation")
                        break
            else:
                print("No such account with the account number you entered was found")
####################
    lets_roll = input(
        "\nIf you want to continue press 1, pressing anything else will terminate :\n")
print("|"*25)
print("|||| * ADIOS AMIGO * ||||")
print("|"*25)
