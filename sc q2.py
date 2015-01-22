def initialise_frequency_array():
    array = []
    return array

def simulate_die_throwing(array):
    import random
    for count in range(20):
        score = random.randint(1,6)
        array.append(score)
    
    return array

    
def display_result_array(array):
    score = "Score"
    frequency = "Frequency"
    print("{0:5} {1:11}".format(score,frequency))
    for counter in range(6):
        freq= 0
        for each in array:
            if each == counter+1:
                freq = freq+1
        print("{0:^5} {1:^11}".format(counter+1,freq))

def main():
    array = initialise_frequency_array()
    array= simulate_die_throwing(array)
    display_result_array(array)
main()
