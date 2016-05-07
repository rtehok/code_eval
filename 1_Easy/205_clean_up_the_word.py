import sys

with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			s = " "
			for i,c in enumerate(line):
				if not(c.isalpha()):
					if (len(s)-1 > 0 and s[len(s)-1] != " ") and i < len(line)-1:
						s += " "
				else:
					s += c.lower()
			
			print(s)