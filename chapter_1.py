sugar_amount = 2
print(f"Initial sugar: {sugar_amount}")

sugar_amount = 12
print(f"Second Initial sugar: {sugar_amount}")

print(f"ID of 2: {id(2)}")
print(f"ID of 12: {id(12)}")

#the above code shows that our object is immutable 
#because when we change the value of sugar_amount, it creates a new object in memory instead of modifying the existing one.
#now to find the output we will type in terminal python chapter_1.py