current_saving = 0
r = 0.04
payment = 25000
semi_annualy_raise = 0.07
Saving_time = 36

#user input
salary = float(input("Enter starting salary "))

# this ps use bisection search
# https://youtu.be/BuwjGi8J5iA
epsilon = 100
low = 0.00
high = 1.00
salary_to_save = (high + low) / 2
number_of_guesses = 0

#in 36 months, each 6 months recive a raise, and interest each month.


