def sort(nums):
    for i in range(len(nums)-1,0,-1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp




nums =[5,7,5,9,3,2,1,4,6,8]
sort(nums)

print (nums)