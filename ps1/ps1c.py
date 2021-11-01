time_so_far = 0
current_saving = 0
r = 0.04
payment = 25000
semi_annualy_raise = 0.07
saving_time = 36
#user input
annual_salary = float(input("Enter starting salary "))

# bisection search
# https://youtu.be/BuwjGi8J5iA
epsilon = 100
low = 0.00
high = 1.00
salary_to_save = (high + low) / 2
number_of_guesses = 0

#in 36 months:
while abs(current_saving - payment) >= epsilon:
    number_of_guesses += 1
    for time_so_far in range(37):
        interest = current_saving * r / 12
        current_saving += annual_salary / 12 * salary_to_save + interest
        print(current_saving)
        time_so_far += 1
        if time_so_far%6 == 0:
            annual_salary += annual_salary * semi_annualy_raise
            monthly_salary_saved = annual_salary / 12 * salary_to_save
    if current_saving > payment:
        high = salary_to_save
    else :
        low = salary_to_save        

