def oddNumbers():
    print("Let's Find The Number Of Even Numbers Between Two Values")
    minVal = int(input('Please Enter Your Lower Value: '))
    maxVal = int(input('Please Enter Your Upper Value: '))
    difference = [*range(minVal + 1, maxVal, 1)]
    counter = []
    for i in difference:
        if (i % 2) == 0:
            counter.append(i)
    print (counter)
    # print('The Even Numbers Between {} and {} are {}'.format(minVal, maxVal, len(counter)))  #different ways of implementing string formatting
    print(f'The Even Numbers Between {minVal} and {maxVal} are {len(counter)}') 

oddNumbers()   




def oddNumbers():
    print("Let's Find The Number Of Odd Numbers Between Two Values")
    minVal = int(input('Please Enter Your Lower Value: '))
    maxVal = int(input('Please Enter Your Upper Value: '))
    difference = [*range(minVal + 1, maxVal, 1)]
    counter = []
    for i in difference:
        if (i % 2) != 0:
            counter.append(i)
    print (counter)
    # print('The Odd Numbers Between {} and {} are {}'.format(minVal, maxVal, len(counter)))   #different ways of implementing string formatting
    print(f'The Odd Numbers Between {minVal} and {maxVal} are {len(counter)}') 

oddNumbers()   