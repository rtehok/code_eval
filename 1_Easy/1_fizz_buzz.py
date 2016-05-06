import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		if len(line.rstrip('\n')) > 1:
			X,Y,N = map(int,line.split(" "))
			arr = []
			for i in range(N):
				i += 1
				if i % X == 0:
					if i % Y == 0:
						arr.append('FB')
					else:
						arr.append('F')
				elif i % Y == 0:
					arr.append('B')
				else:
					arr.append(str(i))
			print(" ".join(arr))