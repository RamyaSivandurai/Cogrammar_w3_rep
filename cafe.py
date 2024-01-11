
############################## Cafe program ################################
print("============================================================ \n")
menu = ['Coffee','Tea','Cake','Coco']  # creating a list called 'menu' that contains all the items sold in the cafe
print(f"The cafe's menu is : {menu}\n")
stock = {'Coffee':20,'Tea':10, 'Cake':30, 'Coco':15}  # creating a dictionary called 'stock' that contain the stock value for each item on the menu
price = {'Coffee':3,'Tea':2, 'Cake':4, 'Coco':3}  # creating a dictionary called 'price' that contain the prices for each item on the menu
total_stock = 0   # inistialising the total_stock result variable
item_value = []   # creating new list for calculating each item's worth


# looping through the menu list and stock,price dictionary to accessing their values 
# calculate each items worth 'item_value' 
# Append the each item value calculated into the 'item_value' list
for item in menu :  
    while item :
        stock_num =stock[item]
        stock_price= price[item]
        item_value.append(stock_num * stock_price)
        break

# calculating the total stock value of all the items in the cafe by adding all the values in the item_value
# used for loop to iterate through and access the item_value and add them together
#store the result in 'total_value' variable
for i in range(len(item_value)):
    total_stock+=item_value[i]


# The code is printing the stock worth of each item in the cafe and the total stock worth.
print(f"Each item's stock worth is : {item_value}\n")
print(f"The total stock worth in the cafe is : {total_stock} \n")

# This print statement and the same one in the beginning of the code is used to make the output more visually appealing and easier to read.
print("============================================================")


