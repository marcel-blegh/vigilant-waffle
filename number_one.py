import random

needsLowerBound = True
needsUpperBound = True
lowerBound = 0
upperBound = 0
target = 0
guess = 0
keepGuessing = True


def get_lower_bound():
    global lowerBound
    global needsLowerBound
    try:
        lowerBound = int(input("Please enter the lower end of the range. "))
        print("Your lower limit is, ", lowerBound)
        needsLowerBound = False
    except:
        print("Sorry, we could not interpret that as an integer. Please try again. ")
        return Exception


def get_upper_bound():
    global upperBound
    global needsUpperBound
    try:
        upperBound = int(input("Please enter the upper end of the range. "))
        print("Your upper limit is, ", upperBound)
        if lowerBound >= upperBound:
            print("The upper end of the range must be larger than the lower end. Please try again. ")
            return
        needsUpperBound = False
    except Exception:
        print("sorry, we could not interpret that as an integer. Please try again. ")
        return Exception


def set_target():
    global lowerBound, upperBound, target
    target = random.choice(range(lowerBound, upperBound))


def guess_number():
    global guess
    print("You are looking for a number between", lowerBound, "and", upperBound - 1)
    guess = int(input("Guess a number "))


def evaluate_guess():
    global guess
    global target
    global upperBound, lowerBound
    global keepGuessing
    if guess == target:
        print("Indeed, the number was ", guess)
        keepGuessing = False
        return
    if guess > target:
        print("Your guess is too high")
        upperBound = guess
    else:
        print("Your guess is too low")
        lowerBound = guess


while needsLowerBound or needsUpperBound:
    try:
        if needsLowerBound:
            get_lower_bound()
        if needsUpperBound:
            get_upper_bound()
    except Exception:
        continue
set_target()

print("We have a value between ", lowerBound, "and ", upperBound, "\n")
print("let's play ...")

while keepGuessing:
    guess_number()
    evaluate_guess()

print("Ready")
