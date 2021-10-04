portion_down_payment = 0.25
current_saving = 0
r = 0.04
# user input:
annual_salary = float(input("Annual salary "))
portion_saved = float(input("Portion saved "))
total_cost = float(input("The cost of the house "))

monthly_salary_saved = annual_salary/12*portion_saved
payment = total_cost*portion_down_payment
interest = current_saving*r/12
t = 0

# #first month
# interest = current_saving*r/12
# current_saving = monthly_salary_saved
# t=1
# print(current_saving)

# # month 2
# interest = current_saving*r/12
# current_saving = monthly_salary_saved + interest
# print(current_saving)
# print(interest)

# #month 3
# interest = current_saving*r/12
# current_saving = monthly_salary_saved + interest
# print(current_saving)
# print(interest)


# from then on
while current_saving < payment:
    interest = current_saving*r/12
    current_saving += monthly_salary_saved + interest
    t += 1
print(t)
