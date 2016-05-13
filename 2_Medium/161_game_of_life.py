import sys

def is_alive(arr,x,y):
	L = len(arr)
	out = []
	alive = 0
	
	for i in range(-1,2):
		for j in range(-1,2):
			try:
				if i ==0 and j == 0:
					pass
				elif x+i >= 0 and y+j >= 0 and arr[x+i][y+j] == "*":
					alive += 1
			except:
				pass
	
	if (arr[x][y] == "*" and alive in (2,3)) or (arr[x][y] == "." and alive == 3):
		return "*"
		
	return "."
	
with open(sys.argv[1], 'r') as test_cases:
	arr = []
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			arr.append(list(line))
			
	for i in range(10):
		arr2 = []
		d = {}
				
		for row in range(len(arr)):
			arr_row = []
			for col in range(len(arr[0])):
				arr_row.append(is_alive(arr,row,col))
			arr2.append(arr_row)
		arr = arr2
	
	for r in arr:
		print("".join(r))