def smallest ( list ):
    min = list[ 0 ]
    for a in list:
        if a < min:
            min = a
    return min

def largest (list):    
    max = list[0]
    for b in list:
        if b > max:
            max=b
    return max        

list = [1, 2, -8, 0 ,-1 ,8 ,9 ,-3]

print ('Smallest:',smallest(list))
print ('Largest:',largest(list))