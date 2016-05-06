import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			x,n = map(int,line.split(","))
			i = 0
			while True:
				i += 1
				if n*i >= x:
					print(n*i)
					break