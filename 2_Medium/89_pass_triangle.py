import sys

with open(sys.argv[1], 'r') as test_cases:
	triangle = []
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			triangle.append([ int(x) for x in line.split(" ") if x != "" ])
	
	for r in range(len(triangle)-2,-1,-1):
		for i in range(len(triangle[r])):
			triangle[r][i] += max(triangle[r+1][i],triangle[r+1][i+1])
			
	print(triangle[0][0])
	