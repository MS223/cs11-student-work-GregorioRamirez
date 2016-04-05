name = raw_input("What's your name?")
upper_bound = input("What's the biggest number you want to guess?")
guess = input("What's your guess?")
import random
random_number = random.randint(0,upper_bound)
while guess != random_number:
    if guess > random_number:
        print "Your answer is too high," + str(name)
        guess = input("What's your guess?")
    else:
        # guess < random
        print "Your answer is too low, " + str(name)
        guess = input("What's your guess?")
    if guess == random_number:
        print "CORRECT !"
        
