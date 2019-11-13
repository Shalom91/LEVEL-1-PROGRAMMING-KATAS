# a function that combines two lists alternately
def combine(lst1, lst2): 
    return [sub[item] for item in range(len(lst2)) 
                      for sub in [lst1, lst2]] 
      
# define lists
lst1 = [11, 22, 33] 
lst2 = [1, 2, 3] 
print(combine(lst1, lst2)) 

combine(lst1, lst2)