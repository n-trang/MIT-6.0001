portion_down_payment = 0.25
current_saving = 0
r = 0.04

# user input:
annual_salary = float(input("Annual salary "))
portion_saved = float(input("Portion saved "))
total_cost = float(input("The cost of the house "))
semi_annualy_raise = float(input("Raise rate every 6 months "))

payment = total_cost*portion_down_payment
t = 0

# this ps use bisection search
# https://youtu.be/BuwjGi8J5iA

