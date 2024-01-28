import argparse
import math
import sys
parser = argparse.ArgumentParser()
parser.add_argument('--type')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--payment')
parser.add_argument('--interest')

args = parser.parse_args()
P = args.principal
n = args.periods
A = args.payment
i = args.interest
loan_type = args.type


if loan_type not in ["annuity", "diff"]:
    print("Incorrect parameters")
elif len(sys.argv) < 5:
    print("Incorrect parameters")
elif loan_type == "diff" and (n is None or P is None):
    print("Incorrect parameters")
elif i is None:
    print("Incorrect parameters")
elif loan_type == 'diff':
    n, P, i = int(n), float(P), float(i) / 12 / 100
    if n < 0 or P < 0 or i < 0:
        print("Incorrect parameters")
    else:
        total_p = 0
        for m in range(1, n + 1):
            D_m = math.ceil(P / n + i * (P - P * (m - 1) / n))
            total_p += D_m
            print(f"Month {m}: payment is {D_m}")
        print(f"Overpayment = {total_p - P}")
elif P is None:
    n, A, i = float(n), float(A), float(i) / 12 / 100
    if n < 0 or A < 0 or i < 0:
        print("Incorrect parameters")
    else:
        principal = math.floor(A / ((i * (1 + i)**n) / ((1 + i)**n - 1)))
        print(f'Your loan principal = {principal}!')
        print(f"Overpayment = {A * n - principal}")
elif A is None:
    n, i, P = float(n), float(i) / 12 / 100, float(P)
    if n < 0 or i < 0 or P < 0:
        print("Incorrect parameters")
    else:
        A = math.ceil(P * ((i * (1 + i)**n) / ((1 + i)**n - 1)))
        print(f'Your annuity payment = {A}!')
        print(f"Overpayment = {A * n - P}")
elif n is None:
    A, i, P = float(A), float(i) / 12 / 100, float(P)
    if A < 0 or i < 0 or P < 0:
        print("Incorrect parameters")
    else:
        n = math.ceil(math.log(A / (A - i * P), i + 1))
        years, months = n // 12, n % 12
        if years == 0:
            print(f'It will take {months} months to repay this loan!')
        elif months == 0:
            print(f'It will take {years} years to repay this loan!')
        else:
            print(f"It will take {years} years and {months} months to repay this loan!")
        print(f"Overpayment = {A * n - P}")
