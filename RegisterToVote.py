"""
Register to Vote
a fun project coded in Python3 by Alan Garcia
"""

# Import all modules necessary to run this program
import time
import datetime
import sys
import webbrowser

# Declare the URL of the register to vote website Vote.org
website = "https://www.vote.org"

# Say an introductory message to the user.
print("Hello! Welcome to my Python program, created by Alan Garcia.")
time.sleep(1)

# Declare a dt function that outputs today's date, and print a formatted message with dt.
dt = datetime.datetime.today()
print('Today is {}/{}/{}'.format(dt.month, dt.day, dt.year))
print()
time.sleep(1)

# Declare a name function that asks for the user's name using the input function
name = str(input("What is your name? "))

# Relay the string inputted by the user into a printed message, with the name function included in between the message
print()
print("Hello " + name + "! Hope you're having an awesome day.")

# Add a two second delay
time.sleep(2)

# Print out another message that introduces the next step of the program
print()
print("I wrote this program to show you my current level of expertise in Python. Let's get started:")

# Add another three second delay
time.sleep(3)


def registered():
    check = str(input("Are you registered to vote? ")).lower().strip()
    try:
        if check[0] == 'y':
            print()
            print("That's great! Don't forget to vote on Election Day, which is on Tuesday, November 5, 2019. You can also early vote!")
        elif check[0] == 'n':
            print()
            print("Let's get you registered to vote!")
            time.sleep(3)
            webbrowser.open(website, 1)
        else:
            print("Sorry, I didn't understand that. Please answer with Y for Yes or N for No.")
            return registered()
    except BaseException as error:
        print("Invalid input.")
        print(error)
        return registered()

# Create a loop that asks the user to enter in their age, and configure two outputs based on whether the person is old enough to vote in the U.S. (>18 years)
while True:
    try:
        # Note: Python 2.x users should use raw_input, the equivalent of 3.x's input
        age = int(input("Please enter your age: "))
    except:
        print("Sorry, I didn't understand that.")
        # Better try again... Return to the start of the loop
        continue
    else:
        # Age was successfully parsed!
        # We're ready to exit the loop.
        break
if age >= 18:
    print()
    print("You are old enough to vote in the United States!")
    time.sleep(2)
    registered()
else:
    print()
    print("You are not old enough to vote in the United States.")

# Add a 1.5 second delay and thank the user for using your program.
time.sleep(4)
print()
print("Thanks for using my Python program! I will now self-destruct in 3 seconds. Goodbye!")

# Self-destruct the program by terminating it without user input.
time.sleep(3)
sys.exit(0)
