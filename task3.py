nums = [int(i) for i in input().split()]
if len(nums) == 1: print(nums[0])
else:
    for i in range(len(nums)):
        x = nums[i-1] + nums[i+1-len(nums)]
        print(x, end = ' ')
