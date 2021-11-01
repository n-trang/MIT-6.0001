# find square root of x
# https://youtu.be/BuwjGi8J5iA

x = float(input("number to find square root of "))
epsilon = 0.01
number_of_guess = 0
low = 0
high = x
ans = (high +low) / 2
while abs(ans**2 -x) >= epsilon:
    print('low', low, 'high', high, 'answer', ans)
    number_of_guess += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
print('numbers of guesses: ', number_of_guess)
print(ans, 'is close to square of root of', x)