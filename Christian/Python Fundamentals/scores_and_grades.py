from itertools import repeat
import random 

for x in repeat(None, 10):
    d = random.randint(60, 100)
    if d in range(60, 70):
        print ("Score: %d; Your grade is D." %(d))
    elif d in range(70, 80):
        print ("Score: %d; Your grade is C." %(d))
    elif d in range(80, 90):
        print ("Score: %d; Your grade is B." %(d))
    elif d in range(90, 101):
        print ("Score: %d; Your grade is A." %(d))
