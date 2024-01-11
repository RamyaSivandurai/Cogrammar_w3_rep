
                    ################# Pseudocode ###################
'''
We have to import math library to do arithmetic calculations for our interest calculator project
Get user input to choose which calculation they want to do.
The output will look like this:
declare calculation _choice
print("Menu to choose for the calculations are: ")
print --> investment-to calculate the amount of interest you'll earn on your investment.
print --> bond-to calculate the amount you'll have to pay on a home loan 
calculation_choice = input(Enter either 'investment' or 'bond' from the menu above to proceed :)
Using lower() will make the selection input into all lowercase letters.
used lower() to get the all the user input  to get validated irrespective of capital and small letters.
if calculation_choice='investment'
  get user input for 
  1.amount of money they are depositing (P)
  2.the interest rate (r=interest/100) getting the interest rate input as float e.g.5.5 
  3.the number of years they plan on investing (t)
  4.ask to input whether 'simple' or 'compound' interest and store it in 'interest' variable
  simple interest formula is A = P*(1+ r*t)
  compund interest formula is A = P* math.pow((1+r),t)
  print the answer A is the total amount once the interest has been applied  with 2 decimal places
elif calculation_choice = 'bond'
  get user input for 
  1.The present value of the house (P)
  2.The interest rate (i= Annual interest rate /12. Annual interest rate = interest rate/100)
  3.The number of months they plan to take to replay the loan (n)
  The bond repayment formula is repayment=(i*P)/(1-(1+i)**(-n))
  calculate the repayment amount and print the answer with 2 decimal places.
else
  print the error message if both investment and bond is not selected.

'''
                    ################### Code ######################

import math  ## using the built-in module called math , which extends the list of mathematical functions
print("==============================================================================")
# getting user input choice 'investment' or 'bond' for calculation
print("Menu to choose for the calculations are: \n")
print("investment-to calculate the amount of interest you'll earn on your investment")
print("bond-to calculate the amount you'll have to pay on a home loan \n")
calculation_choice = ''  # declaring the input choice for calculation
calculation_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed :").lower()

# if the user choice is 'investment'
if calculation_choice == "investment":
    print("\n")  # \n is used to enter an empty line for the output to look neat and tidy
    P = int(input("Enter the amount of money you are depositing:"))
    interest_rate = float(input("Enter the interest rate:"))
    r = interest_rate/100  # calculating the annual interest rate
    t = int(input("Enter the number of years you plan on investing: "))

    # asking user and getting the interest type they like to calculate whether 'simple' or 'compound' interest

    interest = input("Do you want Simple interest or Compound interest(Enter 'simple' or 'compound'):").lower()  ## used lower() to get the all the user input  to get validated irrespective of capital and small letters.
    A=0  ## declaring the final amount of interest you will earn
    ## calculating simple interest
    if interest == "simple":
        A = P*(1+ r*t)            # simple interest formula
        print("\n")
        print(f"The interest amount you will earn for the money you invested is : £ {A:.2f}\n")
        print("==============================================================================")
    ## calculating compound interest
    elif interest == "compound":
        A = P* math.pow((1+r),t)  # compound interest formula
        print("\n")
        print(f"The interest amount you will earn for the money you invested is : £ {A:.2f}\n")
        print("==============================================================================")

# if the user choice is 'bond'       
elif calculation_choice == "bond":
    print("\n")
    P = int(input("Enter the present value of the house:"))
    interest_rate = float(input("Enter the interest rate:"))
    r = interest_rate/100 ### annual interest rate
    i = r/12              ### monthly interest rate
    n = int(input("Enter the number of months you plan to repay the loan:"))
    repayment = 0
    repayment = (i*P)/(1-(1+i)**(-n)) # loan repayment formula
    print("\n")
    print(f"The repayment amount you have to pay each month is : £ {repayment:.2f}\n")
    print("==============================================================================")

# displaying error message if the user inputs neither 'investment' nor 'bond' and inputs something else
else:
    print("You didn't choose 'investment' or 'bond'.  Please Enter a valid input")
    print("==============================================================================")


