# Megan Wheeler
# Assignment 1.3
# 25 October 2024

# Ask the user how many bottles of beer are on the wall.
# Pass that input to a function that manages the countdown.
# The function should take the input and count backwards to 1 while displaying the number of remaining bottles of beer on the wall.
# Once the count is down to 1, change lyrics to show "1 bottle of beer..."
# At the end of the countdown, get back to the main program and remind the user to buy more beer.

def main():

    # Get user input
    bottlesOfBeer = int(input('Enter number of bottles: '))

    # Call function and pass in user input
    countdown(bottlesOfBeer)

# Define countdown function
def countdown(n):

    # Test user input for first condition
    while n > 1:

        # Print first song verse with user input
        print(f'{n} bottles of beer on the wall, {n} bottles of beer.')

        # Decrease n to continue countdown
        n -= 1

        # Print second song verse with decreased value of n
        print(f'Take one down and pass it around, {n} bottle(s) of beer on the wall.')
        print()

    # Test user input for middle condition
    if n == 1: 

        # Print first song verse using 1 instead of n
        print(f'1 bottle of beer on the wall, 1 bottle of beer.')
        
        # Decrease n to continue countdown
        n -= 1

        # Print second song verse using decreased value of n
        print(f'Take one down pass it around, {n} bottle(s) of beer on the wall.')
        print()

    # Test user input for last condition
    if n == 0:
        print('Time to buy more bottles of beer.')
        print()
        print('Terminated with exit code 0.')

if __name__ == '__main__':
    main()