'''Creston Dorothy IDE Lab 2 section 5'''

human_age = float(input("Enter Your age: ")) # Prompts user to enter their age.
dog_age = human_age * 7 
dog_years = dog_age // 1
dog_months = (dog_age % 1) * 12 // 1 
dog_days = (dog_age % 1) * 12 % 1 * 30 // 1

print("Your age in dog years is " , dog_years , ' years' , dog_months , 'months' , dog_days , 'days')

 
cat_age = human_age / 9
cat_years = cat_age // 1
cat_months = (cat_age % 1) * 12 // 1
cat_days = (cat_age % 1) * 12 % 1 * 30 // 1

print("Your age in cat years is " , cat_years , "years" , cat_months , "months" , cat_days , "days")

horse_age = 3 * ((((human_age ** 2) -47) / 7) + 12 )
horse_years = horse_age // 1
horse_months = (horse_age % 1) * 12 // 1
horse_days = (horse_age % 1) * 12 % 1 * 30 // 1

print("Your age in horse years is " , horse_years , 'years' , horse_months , 'months' , horse_days , 'days')
