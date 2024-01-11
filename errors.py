# This example program is meant to demonstrate errors.
 
# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.

print ("Welcome to the error program") # Syntax error print statement is missing parenthesis
print ("\n")                           # Syntax error print statement is missing parenthesis and unexpected indent

    # Variables declaring the user's age, casting the str to an int, and printing the result
age_Str = "24"                         # TypeError alphabet characters can't be casted into an int
age = int(age_Str) 
print("I'm " + str(age) + " years old.") # TypeError can only concatenate str (not "int") to str  so cast age to a str

    # Variables declaring additional years and printing the total years of age
years_from_now = 3                      # TypeError str wont support doing arithmetic so removed ""
total_years = age + years_from_now
print ("The total number of years: " + str(total_years))  # TypeError can only concatenate str (not "int") to str and SyntaxError Print statement is Missing Parenthesis and wrong Variable name used 
# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total_years* 12           # SyntaxError wrong variable name "total" is used instead of "total_years"
print ("In 3 years and 6 months, I'll be " + str(total_months+6) + " months old")  # LogicalError for 3 years and 6 months we have to add 6 to the total_months and TypeError can only concatenate str (not "int") to str 
#HINT, 330 months is the correct answer