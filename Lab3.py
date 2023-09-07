''' Creston Dorothy Intro to Programming
Lab 3 - Selection Statements
9/7/2023'''

user_salary = int(input("Enter the amount of income you earned in 2023:"))

status = input("Are you married or single?\n Type m for married and s for single:")
bracket1 = 0.10
bracket2 = 0.12
bracket3 = 0.22
if (status == ('m') and user_salary > 190750) or (status == ('s') and user_salary > 95375):
	print ("You made too much money for this calculator!")
	
elif user_salary < 11001 and  user_salary > 0 and status == ('s'):
	print("This year you owe" , (user_salary * bracket1) , "in taxes")
	
elif user_salary < 22001 and  user_salary > 0 and status == ('m'):
	print("This year you owe" , (user_salary * bracket1) , "in taxes")
	
elif user_salary >= 11001 and  user_salary < 44726 and status == ('s'):
	print("This year you owe" , (((user_salary - 11000) * bracket2) + 1100) , "in taxes")
	
elif user_salary <= 89450 and  user_salary > 22000 and status == ('m'):
	print("This year you owe" , (((user_salary - 22000) * bracket2) + 2200) , "in taxes")
	
elif user_salary > 44725 and  user_salary <= 95375 and status == ('s'):
	print("This year you owe" , round((((user_salary - 44725) * bracket3) + 1100 + 4047),2) , "in taxes")
	
elif user_salary > 89450 and  user_salary <= 190750 and status == ('m'):
	print("This year you owe" , round((((user_salary - 89450) * bracket3) + 2200 + 8094),2) , "in taxes")
