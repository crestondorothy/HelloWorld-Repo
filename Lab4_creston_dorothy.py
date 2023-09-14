'''Creston Dorothy
Lab 4
Finding deficient, perfect, and abundant numbers.
9/14/2023'''
num = int(input("Enter an upper bound for a check:"))

perfect = 0
abundant = 0
deficient = 0

for i in range(1,num+1):
	divisor = 0
	for j in range(1,i):
		
		if i % j == 0:
			divisor += j
			
	if i == divisor:
		perfect += 1
	elif divisor > i:
		abundant += 1
	else:
		deficient+=1
	
print(f'Between 1 and {num} there are \n {deficient} deficient numbers \n {perfect} perfect numbers \n {abundant} abundant numbers')

	
