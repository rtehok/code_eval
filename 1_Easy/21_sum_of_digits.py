import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			print(sum(map(int,[x for x in line])))