import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			arr = line.split(" ")
			print(" ".join(w for w in reversed(arr)))