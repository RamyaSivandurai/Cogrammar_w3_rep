
############ Pseudocode ##############

'''
we are going to use single for loop and an if else statement
declaring num variable with value 1 to use it to increment star by num value to achieve the star pattern
for loop with range 1,10 for 9 lines of star pattern
if i<6 to print the first 5 lines of the star pattern with ascending '*'
print * times num
num+=1
else to print the last 4 lines of the star pattern with descending '*'
num-=2  
print * times num
num+=1

'''
############ Code #############

num=1   # variable num using to increment '*' one by one
for i in range(1,10):  # single for loop for achieving 9 lines of the star pattern
    if i < 6 :         # to print the first 5 lines of the star pattern with ascending '*'
        print('*' * num)
        num+=1
    else:              # to print the last 4 lines of the star pattern with descending '*'
        num-=2
        print('*'* num )
        num+=1
        


    