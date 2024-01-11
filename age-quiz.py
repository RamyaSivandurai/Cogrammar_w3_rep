
                ######## Pseudocode #######
'''
Get user input for the age as an integer variable
the input age should be less than or equal to 100
if the age is <=13 then print ouput message as "You qualify for the kiddie discount."
elif the age is 21 then print o/p meaasage as "Congrats on your 21st!"
elif the age is >=40 and <65 then print o/p message as "You're over the hill."
elif the age is >=65 and <=100 then print o/p message as "Enjoy your retirement!"
elif the age is >100 then print o/p message as "Sorry,you're dead!"
else for other ages print o/p message as "Age is but a number"
elif stands for else if 
use \n(Escape sequence) for giving empty lines in between the outputs.
'''

                ########### Code ############

print("========== Age Quiz ==========\n" )

age = int(input("Enter your age: "))  # defining the variable age  and assign the value as integer

print("")

if age <= 13:                        # start checking the variable against specific values
    print("You qualify for the kiddie discount.\n") 
elif age == 21:
    print("Congrats on your 21st!\n")
elif age >= 40 and age < 65:
    print("You're over the hill.\n")
elif age >=65 and age <= 100:
    print("Enjoy your retirement!\n")
elif age > 100:                     # age should be <=100 but if you input more than 100 then you get this message
    print("Sorry,you're dead!\n")
else:                               # for all the other ages that doesn't meet the above conditions
    print("Age is but a number\n")

print("==============================")