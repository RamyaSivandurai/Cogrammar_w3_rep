
######## Pseudocode #######
'''
Get user input for name
Get user input for age
Get user input for house number 
Get user input for the street name
Print the details in a single sentence using f" string literal
'''
########### Code ############

# Getting user input of all the details
name = input("Enter your name: ")
age = input("Enter your age: ")
house_number = input("Enter your house number: ")
street_name = input("Enter your street name: ")

print("")

# f" string literal method is used here to print the single sentence with all the details of the user
print(f"This is {name} who is {age} years old and lives at house number {house_number} on {street_name}") 
