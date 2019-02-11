def mean_num_friends(x):
    return round((sum(x)/len(x)),2)

def median_num_friends(x):
    x.sort()
    l=len(x)
    if (len(x)%2!=0):
        median = x[(l-1)//2]
    else:
        median= (x[l//2] + x[(l//2)-1])//2
    
    return (median)    
    
    
num_friends=[100, 49, 41, 40, 25, 10, 5, 4, 7, 20, 60]

mean_num_friends(num_friends)
median_num_friends(num_friends)