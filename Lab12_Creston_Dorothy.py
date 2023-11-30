#Creston Dorothy Recursion Lab
numbers = open("randomValues.txt", 'r')

numlist = []
numlist2 = []
for i in numbers:
	i = i.strip()
	numlist.append(i)

flag = True
for i in numlist:
	try:
		x = int(i)
		numlist2.append(x)
	except ValueError:
		flag = False



def minimum(x):
	if len(x) == 1:
		return x[0]
	rest_min = minimum(x[1:])
	if x[0] < rest_min:
		return x[0]
	else:
		return rest_min
	
		
def maximum(x):
	if len(x) == 1:
		return x[0]
	rest_max = maximum(x[1:])
	
	if x[0] > rest_max:
		return x[0]
	else:
		return rest_max
	
def extrema(nums,mn = True,mx = True):
	if mn == True and mx == True:
		return(f"Minimum value is {minimum(nums)}\nMaximum value is {maximum(nums)}")
	if not mn and mx:
		return(f"Maximum value is {maximum(nums)}")
	if not mx and mn:
		return(f"Minimum value is {minimum(nums)}")
		
numbers.close()
		

