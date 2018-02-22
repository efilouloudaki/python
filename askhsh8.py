import itertools
import random

def random_gen(low,high):
    while True:
        yield random.randrange(low, high)

gen = random_gen(-30,30)

def sum3(gen):
    list=map(str,gen)
    for a in gen:
        for b in gen:
            for c in gen:
                if int(a)+int(b)+int(c)==0:
                     return True
                else:
                    return False