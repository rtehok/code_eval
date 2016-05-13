import fileinput, fractions, functools, operator

#https://github.com/nikai3d/ce-challenges/blob/master/moderate/lucky_tickets.py3

def choose(n, k):
    return int(functools.reduce(operator.mul, (fractions.Fraction(n-i, i+1) for i in range(k)), 1))

for line in fileinput.input():
    m, r = int(line), 0
    for i in range(m//2):
        r += (-1)**i * choose(m, i) * choose(11*m//2-1-10*i, m-1)
    print(r)