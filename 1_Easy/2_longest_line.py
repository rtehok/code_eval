import sys

with open(sys.argv[1], 'r') as test_cases:
	n = -1
	d = dict()
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			if n == -1:
				n = int(line)
				arr = []
			else:
				try:
					d[len(line)].append(line)
				except:
					d[len(line)] = [line]
	
	for k in reversed(sorted(d.keys())):
		for i in range(len(d[k])):
			if n == 0:
				break
			else:
				print(d[k][i])
				n -= 1