class Solution:
    def runningSum(nums):
        numadd = []
        temp = 0
        for i in range(len(nums)):
            temp += nums[i]
            numadd.append(temp)
        return numadd
    
    nums = [1,2,3,4]
    print(runningSum(nums))