shopping_list = [] 
#Setting up an empty list
finished = False
#Setting up a variable and assigning it to False
while not finished:
#Creating a while loop to run until finished equals True
    shopping_item = input("Enter next item (-1 to end list): ")
#Adding an item to the list
    if shopping_item == "-1":
    #An if statement to check if the user wants to end the program
        finished = True
        #re assigning finished to True to end the program 
    else:
        shopping_list.append(shopping_item) #add new item to the list
        
for index, item in enumerate(shopping_list):
   print("Item {0} is {1}".format(index +1,item))
    

