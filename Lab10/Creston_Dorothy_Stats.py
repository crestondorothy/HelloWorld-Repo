#Creston Dorothy Stats

def mean(data):
	count = 0
	total = 0
	for i in data:
		total += i
		count += 1
	return(total/count)

def median(data):
	count = 0
	data.sort()
	for i in data:
		count += 1
	return(data[count//2])
print(median([5,1,2,4,3]))

