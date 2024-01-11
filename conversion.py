
######## Pseudocode #######
'''
Declaring the variables num1,num2,num3,string1 with their values
Converting those variable into different data types using "casting" and assign them to the same variable names as follows:
num1 to int(num1)
num2 to float(num2)
num3 to str(num3)
string1 to int(string1)
Print out all the variables on separate lines using f' string literal print()
'''

########### Code ############

# variables before casting
# 'casting' is used to convert variables from one type to another
num1 = 99.23
num2 = 23
num3 = 150
string1 = "100"

# variables casting part 
num1 = int(num1)
num2 = float(num2)
num3 = str(num3)
string1 = int(string1)
 
# printing the converted output
print(f"num1 = {num1}")
print(f"num2 = {num2}")
print(f"num3 = {num3}")
print(f"string1 = {string1}")
