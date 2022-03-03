import itertools
import math
from col_trans import decode
from fitness_100 import matches
import fetch_email

text = fetch_email.get_mail_5()

def perm(cols, r, index):
    elems = list(itertools.permutations(range(cols), cols))
    return elems[index: index + r]


cols = 10
top_score = 0.6
start = 3306640

max_iterations = math.factorial(cols)
i = 0
combinations = perm(cols, max_iterations, start)
for key in combinations:
    score = matches(decode(text, key))
    if score > top_score:
        top_score = score
        print("High: " + str(top_score) + "[" + str(i+start) + "] for " + str(key))
        print(decode(text, key))
        break
    i += 1