import random

decider_h_or_t = random.randint(1,2)

if decider_h_or_t % 2 == 0:
    print("heads")
else:
    print("tails")
