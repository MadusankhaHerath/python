def binaryS(arr,target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2    # Find the middle index


        # Check if the target is at the mid position
        if arr[mid] == target:
            return mid
        
        # If the target is smaller, narrow down to the left subarray
        elif arr[mid] > target:
            high = mid -1

        # If the target is larger, narrow down to the right subarray
        else:
            low = mid + 1 


    return -1

                 

arr =[1,2,3,4,5,6,7,8,9,10]
target = int(input("input the target number :"))

result = binaryS(arr,target)

if result != -1:
    print(f"element {target} found at index {result} ")

else:
    print(f"element {target} not found")    

    