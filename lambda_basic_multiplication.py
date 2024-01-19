from functools import reduce
arr = []

num = int(input("Enter the size of array="))
for i in range(num):
    nums = int(input("Enter the number ="))
    arr.append(nums)

    
res = reduce(lambda a,b: a*b,arr)
print(res)
