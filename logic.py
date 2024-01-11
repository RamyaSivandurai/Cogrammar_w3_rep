
# This is a program to display a logical error
# This program is meant to find how many chocolates will each child get and print out if the children will get even or odd number of chocolates

total_choc = int(input("Enter the total number of chocolates you have : "))
child_num= int(input("Enter the number of children : "))
per_child_choc = int (total_choc / child_num)
print (f"Each child will get : {per_child_choc} Chocolates")
if (per_child_choc % 2) != 0:   # Logical error -to find even number the logis is %2==0 The ouput will display 6 as an odd number
    print("All the children will get even number of chocolates ")
else:
    print("All the children will get odd number of chocolates ")



