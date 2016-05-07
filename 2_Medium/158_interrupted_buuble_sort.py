import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			arr, n = line.split("|")
			n = int(n.strip())
			arr = [ int(s) for s in arr.split(" ") if s != "" ]
			L = len(arr)
			k = 0
			for i in range(len(arr)-1,1,-1):
				is_sorted = True
				for j in range(i):
					if arr[j] > arr[j+1]:
						tmp = arr[j]
						arr[j] = arr[j+1]
						arr[j+1] = tmp
						is_sorted = False
				if is_sorted:
					break
				k += 1
				if k == n:
					break
			print(" ".join([str(i) for i in arr]))