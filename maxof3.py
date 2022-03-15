"""
Program to compute maximum of three numbers
Example program by Prashant Joshi

Depicts:
Use of a "function"
Use of "if" statement
use of "print" statement with concatenation of various strings + integers
Taking "input" of numbers

"""

# Find the largest
def maximum(num1, num2, num3):

    largest = num1

    if num1 < num2:
        largest = num2

    if largest < num3:
        largest = num3

    return largest

more=1

while (more==1):

    # Get the three numbers from the user
    num1 = int(input('Enter the first number  : '))
    num2 = int(input('Enter the second number : '))
    num3 = int(input('Enter the third number  : '))
    person = input('Enter your name :')

    # Print the largest on the console
    print("\n\t\tHello " + person + " using implemented function the max of the given numbers " \
        + str(num1) + ", " + str(num2) + ", "  \
        + str(num3) + " is : " + str(maximum(num1, num2, num3)))

    # Other way is to use the max function

    print("\nUsing the max function the max of the given numbers " + str(num1) + ", " + str(num2) + ", "  \
        + str(num3) + " is : " + str(max(num1, num2, num3)))
    more=int(input('Got more data to compute? :'))

# End of program