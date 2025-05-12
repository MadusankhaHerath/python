def selection(arr):
    n=len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1,n):
            if arr[j]<arr[min]:
                min = j
            
        arr[i],arr[min] = arr[min],arr[i]
               
        print(arr)


# Test the selection sort function  
arr = [5,3,1,4,2]
print("Before sorting:", arr)
selection(arr)
print("After sorting:", arr)           
