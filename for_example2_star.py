given_number = int(input("Enter a number: \n"))


if given_number % 2==0: # If number is even. 
        stars = "*"
        for i in range(0 ,10):
                print(stars)
                stars = stars +"*"
                
elif (given_number % 2 != 0): # If number is odd, i.e. the number divided by 2 does NOT have a remainder of 0.
        stars = "**********"
        for i in range(0 ,10):
                index = 10-i  # i goes from 0 to 10 in this loop
                print(stars[0:index])