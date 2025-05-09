def insertion(arr):
    for i in range(1,len(arr)):
        key = arr[i]
        j = i - 1
        while arr[j]>key and j>=0:
            arr[j+1] = arr[j]
            j = j -1

        arr[j+1] = key


num = []
print ("enter 5 numbers:")

for i in range(5):
    val = int(input(f"numbers {i + 1}: "))
    num.append(val)

print("befor sorting" ,num)

insertion(num)

print ("after sorting", num)

           
                   