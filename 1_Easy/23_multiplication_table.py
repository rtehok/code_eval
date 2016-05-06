import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			n = int(line)
			r = 1
			while r <= n:
				arr = []
				for i in range(1,n + 1):
					res = str(i*r).rjust(len(str(n*n)))
					arr.append(res)
				print(" ".join(arr))
				r += 1