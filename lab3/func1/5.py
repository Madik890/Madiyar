
from itertools import permutations
def str_per(s):
    for p in permutations(s):
        print (''.join(p))


y = "str"
str_per(y)
