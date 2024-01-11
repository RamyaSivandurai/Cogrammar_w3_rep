
################## Pseudocode ######################

'''
Declare a string variable called sentence = “The!quick!brown!fox!jumps!over!the!lazy!dog.”
Use replace() function to replace the ! with blank space and save it to the sentence.
Print the new sentence output
Using upper() function we are going to turn the sentence into all uppercase and save the result to the sentence
Print the new sentence output
Using string indexing and slicing we are going to reverse all the characters in the new sentence and save it to the variable sentence
Print the new sentence output
'''
###################### Code ##########################

 # printing the original sentence
sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence) 

 # printing the new sentence after the ! is replaced with blank spaces
sentence = sentence.replace('!',' ')
print(sentence) 

# printing the new sentence with all characters in uppercase
sentence = sentence.upper()
print(sentence)  

 # printing the new sentence with all characters in reverse order
sentence = sentence[::-1]
print(sentence) 