"""
Aidan Stout
lab1.py
Problem: creating a program that calculates the monthly interest charge on a credit card account
This program is entirely my own work
"""

def monthly_interest():
    annual_interest = eval(input("Enter your annual interest:"))
    billing_cycle = eval(input("Enter the number of days in your billing cycle:"))
    net_balance = eval(input("Enter your previous (net) balance:"))
    payment = eval(input("Enter the amount paid:"))
    day_paid = eval(input("Enter the day of the billing cycle on which the payment was made:"))
    step1 = net_balance * billing_cycle
    step2 = payment * (billing_cycle - day_paid)
    step3 = step1 - step2
    average_daily_balance = step3 / billing_cycle
    interest = annual_interest / 12 / 100
    monthly_interest_charge = average_daily_balance * interest
    print("Your monthly interest charge is: $", monthly_interest_charge)
