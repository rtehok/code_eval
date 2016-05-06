import sys, math

def is_prime(num):
	k = 2
	n = num ** 0.5
	prime = True
	while k <= n and prime:
		if num % k == 0:
			prime = False
		k += 1
	
	return prime
	
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			arr = []
			i = 2
			n = 1
			while n <= int(line):
				if is_prime(i):
					arr.append(i) 
					n += 1
				i += 1
			
			print(sum(arr))