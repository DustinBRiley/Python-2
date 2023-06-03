# INF360 - Programming in Python
# Dustin Riley
# Assignment 2

import random
users = ["Cody", "Wally", "Jennifer"]
passwords = ["waffles", "password", "jesustakethewheel"]
username = False
password = False
number = False
count = 0
user = 0

print("Please log in.")
while username == False and password == False:  # boolean operator and
    while username == False:        # while loop that conatins a break and continue
        name = input("\nUsername: ")
        for i in range(3):          # for loop using range()
            if name == users[i]:
                username = True
                user = i
                break               # break out of for loop no further iterations needed
        if username == True:        # continue past print(Incorrect username)
            continue
        print("\nIncorrect username.")

    while password == False:
        pw = input("\nPassword: ")
        if pw == passwords[user]:
            password = True
            break
        else:
            print("\nIncorrect password.")

print("\nWelcome " + users[user] + "!")
print("\nGuess the number.")
num = random.randint(0, 30)
while number == False:
    guess = int(input("\nGuess: "))
    if guess == num:                                                           # if statement with 2 elif and 1 else
        print("\nYes " + str(guess) + " is the number! Finally got it")
        number = True
    elif guess < num - 5:                                                      # different comparison operators
        print("No thats too low.")
    elif guess > num + 5:                                                      # different comparison operators
        print("No thats too high.")
    else:
        print("No, but You're close!")

    count += 1

print("\nMan that took " + str(count) + " guesses.")