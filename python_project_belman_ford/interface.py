def print_choose_curr():
    print("Please, choose the currency from the list: \n 1) RUB \n 2) USD \n 3) EUR \n 4) GBP \n 5) BYN \n 6) CNY ")


def print_enter_money():
    print("Enter an initial amount:", end=' ')


def print_balance(money, chosen_currency):
    print(f"Your balance: {money} {chosen_currency}")
