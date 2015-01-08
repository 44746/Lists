def input1():
    message = input("Please enter the message: ")
    cora = input("Is the message in caesar or english? c or e: ")
    if cora == "c":
        shift = -3
    else:
        shift = 3
    return message,shift

def process(message,shift):
    
    list1 = list(message)
    list2 = []
    for index in range(len(message)):
        character = list1[index]
        index= index+1
        ascii_character = ord(character)
        caesar = ascii_character + shift
        character = chr(caesar)
        list2.append(character)
    print(list2)

def main():                      
    message,shift= input1()
    process(message,shift)

main()
