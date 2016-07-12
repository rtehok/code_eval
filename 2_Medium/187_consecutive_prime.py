import sys
PRIMES = set((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31))

def compute(n):
	d = {(1,):set([1])}
	
	while len(list(d.keys())[0]) < n:
		tmp = {}
		for i in range(2,n+1):
			for arr,_set in d.items():
				length = len(arr) + 1
				tmp2 = set(_set)
				if (i not in _set) and (i + arr[-1] in PRIMES) and ((length < n) or (length == n and (1 + i in PRIMES))):
					tmp2.add(i)
					arr += (i,)
					tmp[arr] = tmp2
					
		d = tmp
		
	print(len(d))
	
def compute_rec(n,seq):
	if (len(seq) == n) and ((seq[-1] + 1) in PRIMES):
		return 1
	
	ans = 0
	
	for i in range(2,n+1):
		if i not in seq and seq[-1] + i in PRIMES:
			seq.append(i)
			ans += compute_rec(n,seq)
			seq.pop()
		
	return ans
	
with open(sys.argv[1], 'r') as test_cases:
	# import timeit
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			if n <= 1:
				print(n)
			elif n %2 == 0:
				compute(n)
				print(compute_rec(n,[1]))
			else:
				print(0)
	
# PRIME = set((2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31))

# def is_prime(n):
	# return True if n in PRIME else False

# def swap(arr,i,j):
	# tmp = arr[i]
	# arr[i] = arr[j]
	# arr[j] = tmp
	# return arr

# def calculate(arr, n, from_position):
	# if from_position == n:
		# return 1 if is_prime( arr[0] + arr[n - 1] ) else 0
	
	# count = 0
	# previous_number = arr[from_position - 1]
	# if is_prime(previous_number + arr[from_position]):
		# count += calculate(arr,n,from_position + 1)
	# for pos in range(from_position+2,n,2):
		# if is_prime(previous_number + arr[pos]):
			# arr = swap(arr, from_position, pos)
			# count += calculate(arr,n,from_position + 1)
			# arr = swap(arr, from_position, pos)
	
	# return count
			