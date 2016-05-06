import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n,p1,p2 = map(int,line.split(","))
			n = "{0:b}".format(n)
			L = len(n)
			print(str(n[L-p1] == n[L-p2]).lower())