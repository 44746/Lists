list1= []
item = '1'
while item!= "0":
    item=input("Please add an item to a list: ")
    if item!= "0":
        list1.append(item)

for count in range (len(list1)):
    for count1 in range(count+1, len(list1)):
        if list1[count1]<list1[count]:
            list1[count1],list1[count] = list1[count],list1[count1]

print(list1)



