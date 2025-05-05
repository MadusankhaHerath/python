def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

# c) Read 8 numbers from keyboard
nums = []
print("Enter 8 numbers:")

for i in range(8):
    val = int(input(f"Number {i+1}: "))
    nums.append(val)

print("Before sorting:", nums)

bubble_sort(nums)

print("After sorting:", nums)
