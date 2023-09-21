#Creston Dorothy IDE 5: More nested loops- Inntro to programming 9/21/23
'''
8 x 10 multiplication table

for i in range(1,9):
	for j in range(1,11):
		
		product = i * j
		if product < 10:
			print(f"{product} " ,end=" ")
		else:
			print(f"{product}" ,end=" ")
	print()


#prime number finder

for i in range(1,250+1):
	if i>1:
		for j in range(2,i):
			if i%j == 0:
				break
		else:
			print(i)

#prime finder with the ones unit == 3

for i in range(1,250+1):
	if i>1 and i % 10 == 3:
		for j in range(2,i):
			if i%j == 0:
				break
		else:
			print(i)
		
for i in range(1,250+1):
	divisor = 0
	if i>1:
		for j in range(2,i):
			if i % j == 0:
				divisor += j
				if divisor == i:
					print(divisor)
					break
		else:
			print(i)


# perfect number finder or prime
num = 250

for i in range(1,num+1):
	divisor = 0
	for j in range(1,i):
		
		if i % j == 0:
			divisor += j
	if i == divisor:
		print(divisor)

for x in range(1,250+1):
	if x>1:
		for y in range(2,x):
			if x%y == 0:
				break
		else:
			print(x)
