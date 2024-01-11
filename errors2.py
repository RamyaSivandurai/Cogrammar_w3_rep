# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

animal = "Lion"     # SyntaxError missing quotations for the str Lion
animal_type = "cub"
number_of_teeth = 16

full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth" # SyntaxError missing F for f' string literal and LogicalError misplaced animal_type and number_of_teeth

print (full_spec) # SyntaxError print statement missing Parenthesis