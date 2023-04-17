# Calculating the factorial
def factorial_recursion(num):

    # 0 factorial equals to 1
    if num == 0:
        # Print the result to the console
        print("0! is: 1")

    # Can not calculate the factorial of the numbers which are less than 0
    elif num < 0:
        print('An error has occured!\n')   # Give an error message to the user
        quit()                             # Quit the code

    # Calculate the factorial
    else:
        # A factorial variable for calculation
        factorial = 1

        # Print from 1 to num
        for i in range(1, num+1):
            factorial *= i      # Multiply i with factorial on every step of i (*=)

        # Print the result to the console
        print(f'{num}! is: {factorial}')

        # There goes the recursive call
        factorial_recursion(num-1)



# Run the program
factorial_recursion(4)
