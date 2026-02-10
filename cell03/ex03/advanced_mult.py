tablei = 0

while tablei <= 10:
    print ("Table de", tablei, end=": ")

    num = 0
    while num <= 10:
        print (tablei * num,end=" ")
        num += 1
    print()
    tablei +=1