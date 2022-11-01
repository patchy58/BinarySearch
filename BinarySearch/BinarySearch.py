def binary_search(list1, n):  
    low = 0  
    high = len(list1) - 1  
    
  
    while low <= high:  
        mid = (high + low) // 2  
  
        if list1[mid] < n:  
            low = mid + 1  
  
        elif list1[mid] > n:  
            high = mid - 1  
  
        else:  
            return mid  
  
    return -1  
  
  
 
lst = [1, 4, 7, 12, 15, 19, 21, 24]  
target = 19 
  
 
result = binary_search(lst, target)  
print(result)

