import sys, math

def find_cycle(seq):
	d = {}
	
	for i,v in enumerate(seq):
		if v in d:
			return map(str,seq[d[v]:i])
		d[v] = i

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			arr = list(map(int,line.split(" ")))
			print(" ".join(find_cycle(arr)))