
################### Pseudocode #############
'''
writing a code to use the string manipulation method strip()
Declaring a string variable called hero that contains value "$$$Superman$$$"
Using f'string in displaying the outputs for the style. 
Use strip() on hero to remove all $ from its start and end and save the output to the variable hero
Print hero now to get the new ouput
use \n(Escape sequence) for giving empty lines in between the outputs.

'''

#################### Code ##################

hero = "$$$Superman$$$"
print(f"The string is {hero}\n")             #  printing the original hero value

hero = hero.strip('$')                       #  strip() method is used to remove $ from the starting and end of the string value stored in the variable hero
print(f"The manipulated string is {hero}\n") #  printing the new output after manipulating(strip($))
