

########### Program to make alternate characters and words uppercase and lowercase ############## 

print("***************************************************************************************************************") # this print statement is for output styling purpose
                                                                                                                        

real_string = "Python is my favorite language"  
print(f"The real string is: {real_string}")   #print the input string

new_list_1 = list(real_string)     # casting the string to a list to carry out the actions as string is immutable.
# like this ---> new_list_1 = ['P', 'y', 't', 'h', 'o', 'n', ' ', 'i', 's', ' ', 'm', 'y', ' ', 'f', 'a', 'v', 'o', 'r', 'i', 't', 'e', ' ', 'l', 'a', 'n', 'g', 'u', 'a', 'g', 'e']

new_list_2 = real_string.split()   # casting the string to list with split() method to get each words in a list
# like this ---> new_list_2 = ['Python', 'is', 'my', 'favorite', 'language']

# Assigning new lists to save the output after alternating the characters and words
output1 = []  
output2 = []

## making alternate characters uppercase and lowercase characters
#  to convert the alternate charcters to upper we are checking the charcters index position 'index'
#  if the 'index' is even then convert that letter into uppercase or else into lowercase
for index  in  range(len(new_list_1)):
    if index %2 == 0:   # checking for even position
        output1.append(new_list_1[index].upper())  # Append the converted characters to the output
    else:
        output1.append(new_list_1[index].lower())  # converting into lowercase
print("\nThe converted string with alternate character uppercase character and other alternate character lowercase : ")
print("".join(output1))  ## using join method we join the splitted string snd print the otput as a singe string

## making alternate words lowercase and uppercase
#  we are checking the index position of the word 'index'
#  if the 'index' is even then convert the word into lowercase or else into uppercase
for index in range(len(new_list_2)):
    if index %2 == 0:   #checking for even postion
        output2.append(new_list_2[index].lower())   #  convert the current word into lowercase
    else: 
        output2.append(new_list_2[index].upper())  #convert the current word into uppercase
print("\nThe converted string with alternate word lowercase and uppercase : ")
print(" ".join(output2))   ## using join method we join the splitted string into a single string with whitespaces inbetween and print the output
print("*************************************************************************************************************")