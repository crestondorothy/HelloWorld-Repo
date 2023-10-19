"""
Creston Dorothy
Lab 8
Functions and List review
"""




#Problem 1
'''
def calc_toll(hour, is_morning, is_weekend):
	total = 0
	if (is_morning == True) and (is_weekend == False):
		if hour < 7:
			total = 1.15
		elif hour < 10 and hour >= 7:
			total = 2.95
		elif hour >= 10 and hour <= 11:
			total =1.9
	if is_morning == False and  is_weekend == False:
		if hour >= 1 and hour < 3:
			total = 1.9
		elif hour >= 3 and hour < 8:
			total = 3.95
		elif hour >= 8:
			total = 1.4
	if is_morning == True and is_weekend ==  True:
		if hour < 7:
			total = 1.05
		elif hour >= 7 and  hour <= 11:
			total = 2.15
	if is_morning == False and is_weekend == True:
		if hour == 12 or hour < 8:
			total = 2.15
		elif hour < 12 and hour >= 8:
			total = 1.1
	return(total)
		

'''

'''
#Problem 2
def LCM(num1,num2):
	max = 0
	if num1 > num2:
		max = num2
		while max <= num1 * num2:
			if max % num1 == 0 and max % num2 == 0:
				print(f'lcm = {max}')
				break
			else:
				max += 1
	else:
		max = num2
		while max <= num1 * num2:
			if max % num1 == 0 and max % num2 == 0:
				print(f'lcm = {max}')
				break
			else:
				max += 1
	return(max)

'''

		

#Problem 3


def factorial(n):
	f = 1
	if n >= 1:
		for i in range(1,n+1):
			f = f*i		
	return(f)

def combination(m,k):
	c = factorial(m) / (factorial(k) * factorial(m-k))
	return(c)
	
	



if __name__ == '__main__':
	#print(calc_toll(8, True, False))  #answer 2.95
	#print(calc_toll(1, False, False)) #answer 1.9
	#print(calc_toll(3, False, True))  #answer 2.15
	#print(calc_toll(5, True, True))   #answer 1.05


	
	
	#if LCM(10,25) == 50:
		#print("LCM(10,25) is correct")
	#else:
		#print(f"LCM(10,25) is incorrect.  You got {LCM(10,25)}, but the correct answer should be 50.")
	#if LCM(90,342) == 1710:
		#print("LCM(90,342) is correct")
	#else:
	#	print(f"LCM(90,342) is incorrect. You got {LCM(90,342)}, but the correct answer should be 1710.")
	#if LCM(45,240) == 720:
	#	print("LCM(45,240) is correct")
	#else:
		#print(f"LCM(45,240) is incorrect.  You got {LCM(45,240)}, but the correct answer should be 720.")
	



		
	for i in range(10):
		for j in range(i+1):
			print(int(combination(i,j)), end=' ')
		print()






