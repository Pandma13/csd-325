import csv

# Imported both os and sys to tell script where to find csv file
import os
import sys

from datetime import datetime

from matplotlib import pyplot as plt

# Changed to tell script where to find csv file
filename = os.path.dirname(sys.argv[0]) + '/sitka_weather_2018_simple.csv'

# Display menu instructions for user
print('Daily Temperatures - 2018')
print('-------------------------')
print('Enter Highs to see the graph of high temperatures.')
print('Enter Lows to see the graph of low temperatures.')
print('Enter Exit to close the program.')


while True:  # Added loop

    # Get input from user
    tempSelect = input('> ')

    # High temperatures condition
    if tempSelect == 'Highs':

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and high temperatures from this file.
            dates, highs = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                high = int(row[5])
                highs.append(high)

        # Plot the high temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, highs, c='red')

        # Format plot.
        plt.title("Daily high temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        # Dsiplay graph and clear data
        plt.show()
        plt.close()

    # Low temperature condition
    elif tempSelect == 'Lows':

        with open(filename) as f:
            reader = csv.reader(f)
            header_row = next(reader)

            # Get dates and low temperatures from this file.
            dates, lows = [], []
            for row in reader:
                current_date = datetime.strptime(row[2], '%Y-%m-%d')
                dates.append(current_date)
                low = int(row[6])
                lows.append(low)

        # Plot the low temperatures.
        fig, ax = plt.subplots()
        ax.plot(dates, lows, c='blue')

        # Format plot.
        plt.title("Daily low temperatures - 2018", fontsize=24)
        plt.xlabel('', fontsize=16)
        fig.autofmt_xdate()
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis='both', which='major', labelsize=16)

        # Display graph and clear data
        plt.show()
        plt.close()

    # Exit condition
    elif tempSelect == 'Exit':

        # Exit message
        print('Goodbye.')

        # Exit program
        sys.exit()

    # Final condition
    else:

        # Error message
        print("Please enter 'Highs', 'Lows', or 'Exit'.")
