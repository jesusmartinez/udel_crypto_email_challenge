import itertools
import math
from col_trans import col_trans_dec
from fitness import fitness,andy_fitness, matches
import fetch_email

# text = 'dthbaetseynsi'
text = fetch_email.get_mail_5()
# r = number of combinations to get back
# index = where to start
def nth_combination(iterable, r, index):
    """Equivalent to list(combinations(iterable, r))[index]"""
    pool = tuple(iterable)
    n = len(pool)
    if r < 0 or r > n:
        raise ValueError
    c = 1
    k = min(r, n-r)
    for i in range(1, k+1):
        c = c * (n - k + i) // i
    if index < 0:
        index += c
    if index < 0 or index >= c:
        raise IndexError
    result = []
    while r:
        c, n, r = c*r//n, n-1, r-1
        while index >= c:
            index -= c
            c, n = c*(n-r)//n, n-1
        result.append(pool[-1-n])
    return tuple(result)

def perm(cols, r, index):
    # iter = itertools.permutations(range(cols), cols)
    # return [list(i) for i in nth_combination(iter, r, index)]
    elems = list(itertools.permutations(range(cols), cols))
    return elems[index: index + r]

def get_scores(text, keys):
    scores = []
    for key in keys:
        result = col_trans_dec(text, key)
        scores.append(matches(result))
    return scores

# Tune these three parameters
cols = 10
top_score = 0.5
loop_size = 1000
start = 1

batch = 20
index = 1
total_combinations = math.factorial(cols)

# max_iterations = 10000
# iterations = 0
span = (total_combinations - batch) // loop_size
# while top_score <= 0.84 or iterations < max_iterations:
for i in range(loop_size):
    index = start + (i * span)
    combinations = perm(cols, batch, index)
    scores = get_scores(text, combinations)
    if max(scores) > top_score:
        top_score = max(scores)
        pivot = scores.index(top_score) #Just to read the index
        print("High: " + str(top_score) + "[" + str(index) + "] for " + str(combinations[pivot]))
        print(col_trans_dec(text, combinations[pivot]))
    # iterations += 1
    # start = top *

# print(scores)
# for c in combinations:
