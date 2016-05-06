import sys, math

def is_prime_palindrome(n):
	s_n = str(n)
	l = len(s_n)
	pivot = math.floor(l/2)
	if l % 2 == 0:
		return False
	elif s_n[0:pivot] == s_n[pivot+1:] and n % 2 != 0 and is_prime(n):
		return True
	else:
		return False
		
def is_prime(num):
	prime = True
	k = 2
	n = num ** 0.5
	while k <= n and prime:
		if num % k == 0:
			prime = False
		k += 1
	return prime
	
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			for i in reversed(range(n+1)):
				if is_prime_palindrome(i):
					print(i)
					break