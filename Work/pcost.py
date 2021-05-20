# pcost.py
#
# Exercise 1.27


def portfolio_cost(filename):
    ...
    # Your code here
    ...
    f = open(filename,'rt')
    tc = 0
    hdrs = next(f)
    for line in f:
        r = line.split(',')
        tc += int(r[1])*float(r[2])
    print("Total cost",tc)
