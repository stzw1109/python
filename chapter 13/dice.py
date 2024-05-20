import random

rng = random.Random()

dice_throw = rng.randrange(1, 7)    # Return a random integer N such that a <= N <= b
delay = rng.random() * 5.0

print('Throwing a dice...')
print('The dice shows', dice_throw)