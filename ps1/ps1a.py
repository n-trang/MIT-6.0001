portion_down_payment = 0.25
current_saving = 0
r = 0.04

# user input:
annual_salary = float(input("Annual salary "))
portion_saved = float(input("Portion saved "))
total_cost = float(input("The cost of the house "))

monthly_salary_saved = annual_salary / 12 * portion_saved
payment = total_cost * portion_down_payment
interest = current_saving * r / 12
saving_time = 0

while current_saving < payment:
    interest = current_saving * r / 12
    current_saving += monthly_salary_saved + interest
    saving_time += 1
print(saving_time)
