#l = array of ints
def bubbleSort(l):
    i = len(l)
    if i == 0 or i == 1:
        return("not enough elements to sort!!")
    else:
        sorted = False
        while sorted == False:
            sorted = True
            for x in range(0, i-1):
                if l[x]>l[x+1]:
                    print(f"{l[x]} is bigger than {l[x+1]}")
                    l[x], l[x+1]=l[x+1],l[x]
                    print(l)
                    sorted = False
            i-=1 #we know the last element is sorted
        return l
                
print(bubbleSort([1,2,3,4,5]))
        
    
        