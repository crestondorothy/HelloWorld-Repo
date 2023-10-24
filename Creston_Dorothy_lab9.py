#Creston Dorothy Laby 9 IDE

groceryList = []
costOfItem = []
groceryDict = {}
item = ''
cost = 0
total = 0
while item != "DONE":
	item = input("Enter Your groceryList item:")
	if item == 'DONE':
		print(f"My grocery list is {groceryList}")
		print(f"Cost for each item is {costOfItem}")
		print(groceryDict)
		print(f"Total amount spent on grocery shopping is {total}")
	else:
		cost = int(input())
		groceryList.append(item)
		costOfItem.append(cost)
		groceryDict[item] = cost
		total += cost
				
groceryDict2 = {'a':1,'b':2,'c':3}

def check1(a,b):	
	for i in a:
		if i not in b or b[i] != a[i]:
			return('no')
	for i in b:
		if i not in a or a[i] != b[i]:
			return('no')
	else:
		return('yes')
		
		
print(check1(groceryDict,groceryDict2))





def pricecheck(purchase1,purchase2):
	for i in purchase1:
		if i not in purchase2:
			print(f'{i} is only in purchase1.')
		if i in purchase2 and purchase2[i] > purchase1[i]:
			print(f'{i} is cheaper on purchase1.')
	for i in purchase2:
		if i not in purchase1:
			print(f'{i} is only in purchase2.')
		if i in purchase1 and purchase1[i] > purchase2[i]:
			print(f'{i} is cheaper on purchase2.')
		


print(pricecheck(groceryDict,groceryDict2))

grocerypurchase3 = {'apple':[1,2], 'orange':[5,2] , 'berry': [7,9]}
n = 0
for i in grocerypurchase3:
	
	if grocerypurchase3[i][0] > 1:
		print(f'Purchase {grocerypurchase3[i][n]} {i}s at {grocerypurchase3[i][n+1]} dollars each.')
	elif grocerypurchase3[i][0] == 1:
		print(f'Purchase {grocerypurchase3[i][n]} {i} at {grocerypurchase3[i][n+1]} dollars each.')


