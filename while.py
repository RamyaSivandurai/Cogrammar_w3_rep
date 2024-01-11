
################### Pseudocode #################
'''
# A While loop executes a sequence of statements that are continually repeated while a certain condition is met.

Initialising all the variables 
i = 0 
sum = 0
average = 0
num = 0
using While loop set the condition as i!=-1
while the while loop condition is True 
ask the user continually to enter a number and store it in i as int
if i != -1
num+=1
sum+=i
continue until the user enters -1. when -1 is entered the if loop breaks and takes you to the next while iteration
while loop checks the condition which is False then it breaks the loop
and calculate average = sum / num excluding the -1 just entered
print the average value as output

'''

################### Code ####################

i = 0       # initialising all the variables
sum = 0
num =0
average = 0
while i != -1:      # while loop iterates while the user not entering -1
    i = int(input("Please enter a number : "))
    if i != -1:
        num+=1      # num += 1 is equivalent to num = num + 1
        sum+=i
        continue    # if this if condition becomes False the continue will take you to the next while loop iteration
## calculating average excluding -1 when while loop breaks 
average = sum / num  
print(f"The average of the numbers you entered is {average} ")
