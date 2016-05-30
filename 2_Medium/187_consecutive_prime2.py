import sys

PRIMES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31)

def calculate(n,last_bead,previous_beads,len,ans):
	if len == n:
		if last_bead + 1 in PRIMES:
			ans += 1
		return ans
	for i in range(2,n+1):
		if (i not in previous_beads) and (i + last_bead in PRIMES):
			previous_beads.append(i)
			ans = calculate(n,i,previous_beads,len+1,ans)
			previous_beads.pop()
	
	return ans
	
with open(sys.argv[1], 'r') as test_cases:
	# import timeit
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			if n == 0:
				print(0)
			if n == 1:
				print(1)
			# arr = [ i for i in range(1,n+1) ]
			else:
				print(calculate(n,1,[],1,0))