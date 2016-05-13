import sys

# def is_prime2(n):
	# if n <= 1:
		# return False
	# elif n <=3:
		# return True
	# elif n % 2 == 0 or n % 3 == 0:
		# return False
	# else:
		# i = 5
		# while i*i < n:
			# if n % i == 0 or n % (i+2) == 0:
				# return False
			# i += 6
		# return True

				
# def has_consecutive_prime(arr):
	# i = 0
	# if not(is_prime(arr[0] + arr[-1])):
		# return False
		
	# while i+1 <= len(arr)-1:
		# if is_prime(arr[i]+arr[i+1]):
			# pass
		# else:
			# return False
		# i += 1
	
	# return True
		
# def old():
	# arr = []
	# for line in test_cases:
		# line = line.rstrip('\n')
		# if len(line) > 0:
			# n = int(line)
			# arr = []
			# count = 0
			# list_signature = []
			# if n % 2 == 0:
				# for elt in itertools.permutations(range(1,n+1),2):
					# if is_prime(sum(elt)):
						# arr.append(elt)

				# for elt in itertools.combinations(arr,n//2):
					# flat = [item for sub in elt for item in sub]
					# if len(set(flat)) == n and has_consecutive_prime(flat):
						# signature = "".join(map(str, flat))
						# is_not_duplicate = True
						# for s in list_signature:
							# if s.find(signature) >= 0:
								# is_not_duplicate = False
								
						# if is_not_duplicate:
							# count +=1
							# list_signature.append(signature*2)
							
				# print(count)
			# else:
				# print(0)

PRIME = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
def is_prime(n):
	return True if n in PRIME else False

def swap(arr,i,j):
	tmp = arr[i]
	arr[i] = arr[j]
	arr[j] = tmp
	return arr

def calculate(arr, n, from_position):
	if from_position == n:
		return 1 if is_prime( arr[0] + arr[n - 1] ) else 0
	
	count = 0
	previous_number = arr[from_position - 1]
	if is_prime(previous_number + arr[from_position]):
		count += calculate(arr,n,from_position + 1)
	for pos in range(from_position+2,n,2):
		if is_prime(previous_number + arr[pos]):
			arr = swap(arr, from_position, pos)
			count += calculate(arr,n,from_position + 1)
			arr = swap(arr, from_position, pos)
	
	return count
	
with open(sys.argv[1], 'r') as test_cases:
	# import timeit
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			arr = [ i for i in range(1,n+1) ]
			print(calculate(arr,n,1))
			#print(timeit.timeit("calculate(arr,n,1)", setup="from __main__ import calculate, arr, n"))
			