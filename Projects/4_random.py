import random

random_number = random.random()
print("Random number is:", random_number)

if random_number < 0.25:
    print("Try going right")
elif random_number > 0.25 and random_number < 0.5:
    print("Try going left")
elif random_number > 0.5 and random_number < 0.75:
    print("Try going up")
else:
    print("Try going down")