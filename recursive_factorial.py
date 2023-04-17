# Finding factorial with recursive
def find_factorial(num):

    # 0! is 1
    if num == 0:
        return 1

    # Calculate the factorial
    else:
        return num * find_factorial(num - 1)

    
    
# Num variable is the number you want to calculate the factorial of
num = 5

# Printing the result to the user
print(f'The factorial of {num} is :  {find_factorial(num)}')
