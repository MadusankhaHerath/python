
def bubbles(arr):
    n = len(arr)
    for i in range (n-1):
        for j in range(n-i-1):
            if arr[j]>arr[j+1]:
                arr[j].arrr[j+1] = arr[j+1], arr[j]

num =[]
print("enter 5 numbers")

for i in rangr(5):
    val = int(input(f"number {i+1}:"))
    num.append(val)

    print("before sorting", num)
    bubbles(num)
    print("after sorting", num)
