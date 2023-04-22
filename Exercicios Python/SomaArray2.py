def somaarray(nums, target):
  n = len(nums)
  for i in range(n):
    for j in range(i+1, n):
      if nums[i] + nums[j] == target:
              return [i, j]

ns = [1,2,3,4,5,6]
t = 8
print(somaarray(ns, t))