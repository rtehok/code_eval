import sys

def fib(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	if n >= 2:
		return fib(n-1) + fib(n-2)
	

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			print(fib(n))