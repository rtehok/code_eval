import sys

def str_to_int(arr):
	for row in arr:
		yield list(map(int,row))
			
def get_sum(arr,n,dir):

	if dir == "LEFT" or dir == "UP":
		i = 0
		while i < n:
			if i+1 <= n-1 and arr[i] == arr[i+1]:
				yield arr[i] + arr[i+1]
				i+=1
			else:
				yield arr[i]
				
			i += 1
	else:
		i = n-1
		while i >= 0 :
			if i-1 >= 0 and arr[i] == arr[i-1]:
				yield arr[i] + arr[i-1]
				i-=1
			else:
				yield arr[i]
				
			i -= 1

def put_zeroes(arr,n,dir):
	if dir == "RIGHT" or dir == "DOWN":
		return [0]*(n-len(arr)) + arr
	else:
		return arr + [0]*(n-len(arr))
			
def pivot(arr,n):
	for col in range(n):
		tmp = []
		for row in range(n):
			tmp.append(arr[row][col])
		yield tmp
			
with open(sys.argv[1], 'r') as test_cases:
	for line in test_cases:
		line = line.rstrip('\n')
		if len(line) > 0:
			dir,n,arr = line.split(";")
			n = int(n)
			arr = [ x.strip().split(" ") for x in arr.split("|") ]
			arr = list(str_to_int(arr))
			
			if dir == "DOWN" or dir == "UP":
				arr = list(pivot(arr,n))
				
			out = ""
			out_tmp = []
			for row in arr:
				tmp = [ i for i in row if i != 0 ]
				tmp = put_zeroes(tmp,n,dir)
				tmp = list(get_sum(tmp,n,dir))
				if dir == "DOWN" or dir == "RIGHT":
					tmp = tmp[::-1]
				tmp = put_zeroes(tmp,n,dir)
				if dir == "DOWN" or dir == "UP":
					out_tmp.append(tmp)
				else:
					out += "|" + " ".join(list(map(str,tmp)))
			
			if len(out_tmp) > 1:
				out_tmp = list(pivot(out_tmp,n))
				
				for row in out_tmp:
					out += "|" + " ".join(list(map(str,row)))
			
			print(out[1:])