#George West
#09-1-15
#Hangman

list1 =[]
list2 = []
string = input("Please enter a string: ")

for each in string:
    list1.append(each)
    list2.append("-")

    



count =0
word = False
while word != True:
    search_item = input("Please enter the item you want to search for: ")
    if list1[count] == search_item:
        list2.insert(count, search_item)
        list2.pop(count+1)
    count = count+1
    print(list2)
    found = input("Is the word found?: ")
    if found == "y":
        word = True
  
    

