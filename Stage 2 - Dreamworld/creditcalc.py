import math


def calculate_months(principal, payment):
    months = math.ceil(principal / payment)
    return months


def calculate_payment(principal, months):
    payment = math.ceil(principal / months)
    last_payment = principal - (months - 1) * payment
    return payment, last_payment


def main():
    principal = int(input("Enter the loan principal:\n"))
    calculation_type = input("""
    What do you want to calculate?
    type "m" - for number of monthly payments,
    type "p" - for the monthly payment:\n""")

    if calculation_type == "m":
        monthly_payment = int(input("Enter the monthly payment:\n"))

        months = calculate_months(principal, monthly_payment)

        if months == 1:
            print("It will take 1 month to repay the loan")
        else:
            print(f"It will take {months} months to repay the loan")

    elif calculation_type == "p":
        num_of_months = int(input("Enter the number of months:\n"))

        monthly_payment, last_payment = calculate_payment(principal, num_of_months)

        if last_payment == monthly_payment:
            print(f"Your monthly payment = {monthly_payment}")
        else:
            print(f"Your monthly payment = {monthly_payment} and the last payment = {last_payment}.")


main()
