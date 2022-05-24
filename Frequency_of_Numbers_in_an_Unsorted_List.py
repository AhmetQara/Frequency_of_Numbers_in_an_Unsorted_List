import random
import collections

myList = []

while True:
    
    limit = 0
    
    number = int(input("How many numbers do you want to generate? : "))

    for i in range(number):
        
        myList.append(random.randint(0,9))
        
        print(myList[i], "-", end=" ")
        limit+=1
        
        if limit == number:
            counter=collections.Counter(myList)
            print("\nMost used integer [(integer, frequency)] --> ",counter.most_common(1))
    break
        
           
    

 