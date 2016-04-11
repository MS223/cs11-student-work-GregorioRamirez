import random

def mystery_function(x, y):
    random_number = random.randint(0,2) # What's the range of randoms? The range of randoms is 3.
    if random_number > 0: # What's the probability that random_number is greater than 0? 2 out of 3.
        z = x + y
    else:
        z = x * y
    return z
mystery_function(1, 2)
