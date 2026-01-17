
def get_the_sum(input1, input2):
    sum_val = input1 + input2
    print(sum_val)


a = 25
b = 18
get_the_sum(a, b)



def get_the_sum_with_return(input1, input2):
    sum_val = input1 + input2
    print(sum_val)
    return sum_val


a = 21
b = 41
c = 61
d = 67

print(get_the_sum_with_return(a, b) + get_the_sum_with_return(c, d))


import time


def countdown():
    print("Counting down: ")
    for i in range(10, 0, -1):
        time.sleep(0)
        print(i)
    print("Countdown Finished!")




import time
import os

amount = 0
balance = 10000
pin_code = "2026"


def welcome_message():
    print("_ _ _ _ _ _ _ _ _ _")
    print("Welcome To Christopher's Secure Bank")
    print("- - - - - - -")
    print("Please Insert Your Card")


def card_reader(card_is_inserted):
    if card_is_inserted == "Yes":
        print("Your card is inserted")
        return True
    else:
        print("Your card is NOT inserted")
        return False


def check_pin():
    for i in range(4):
        if i == 3:
            print("Your Card Is Blocked, Contact Your Bank")
            return False
        enter_pin = input("Enter the Pin Number: ")
        if enter_pin == pin_code:
            return True
        else:
            print("Pin Number Error")


def transaction_selection():
    transaction = input("Select: Withdraw | Check Balance: ")
    return transaction


def transaction_validation(withdraw_amount, current_balance):
    if current_balance >= withdraw_amount:
        return True
    else:
        print("Not Enough Balance")
        return False


def card_ejection():
    print("Card Ejected. Please take your card.")


def cash_dispensing():
    print("Cash dispensing, Please Wait...")


def print_receipt(withdraw_amount):
    global balance
    balance = balance - withdraw_amount
    print("Your Remaining Balance is:", balance)
    print("Amount Withdrawn: ", withdraw_amount)
    print("Please take your receipt.")


while True:
    welcome_message()
    card_status = input("Is The Card Inserted? (Yes/No)? ")
    if not card_reader(card_status):
        continue

    if not check_pin():
        break

    selected = transaction_selection()

    if selected == "Withdraw":
        amount_to_get = int(input("Enter Amount: "))
        if transaction_validation(amount_to_get, balance):
            print("Withdraw Transaction Authorized")
            card_ejection()
            cash_dispensing()
            print_receipt(amount_to_get)
        else:
            card_ejection()
            continue

    elif selected == "Check Balance":
        print("Your Current Balance is:", balance)
        card_ejection()
    else:
        print("Invalid Selection")
        card_ejection()
        continue

    break