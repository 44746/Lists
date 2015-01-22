scores = [18,23,36,21,58,40,45,59]
max = 8
for count1 in range(max-1):
    for count2 in range(max-1):
        if scores[count2]>scores[count2+1]:
            temp = scores[count2]
            scores[count2] = scores[count2+1]
            scores[count2+1] = temp
for index in range(len(scores)):
    print(index+1,scores[index])


