
list1= []
item = '1'
while item!= "0":
    item=input("Please add an item to a list: ")
    if item!= "0":
        list1.append(item)

no_swaps=False 
while no_swaps != True:
    no_swaps= True
    for count in range (len(list1)-1):
        if list1[count]> list1[count+1]:
            no_swaps = False
            list1[count+1],list1[count] = list1[count],list1[count+1]

print(list1)
