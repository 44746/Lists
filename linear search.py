#George West
#09-1-15
#Linear Search
def input_values():
    search_list =[]
    item = "1"
    while item!= "0":
        item=input("Please add an item to a list: ")
        if item!= "0":
            search_list.append(item)
    search_item = input("Please enter the item you want to search for: ")
    return search_list,search_item


def linear_search(search_list,search_item):
    found = False
    count =0
    while not found and count<len(search_list):
        if search_list[count] == search_item:
            print("Found")
            found = True
        else:
            print("Not found")
        count = count + 1
    return found

    
def main():
    search_list,search_item = input_values()
    linear_search(search_list,search_item)

main()
