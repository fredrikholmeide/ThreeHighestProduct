#Iterating three times for each max value in the list
#For each max value the algortihm iterates throug the list to locate
#the index of the max value. When located the algortihm pops the
#integer at that index and updates x (product of the current highest)
def ProductThreeHighest(list):
    x = 1
    for i in range(3):
        highest = max(list)
        for i in range(len(list)):
            if highest == list[i]:
                x *= list.pop(i)
                break
    return x
