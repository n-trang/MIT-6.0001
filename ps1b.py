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

#everything that's gonna be updated need to be put into while loop.
while current_saving < payment:
    interest = current_saving * r / 12
    current_saving += monthly_salary_saved + interest
    t += 1
    if t%6 == 0:
        annual_salary += annual_salary * semi_annualy_raise
        monthly_salary_saved = annual_salary / 12 * portion_saved
        print('new salary ', annual_salary)

print(t)