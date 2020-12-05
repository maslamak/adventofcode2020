fname='input_1.txt'
f=open(fname)
nums = f.readlines()
nums = [int(i) for i in nums]
target=2020
flag=False
for ind_1, num_1 in enumerate(nums):
    for ind_2 in range(ind_1, len(nums) ):
        num_2=nums[ind_2]
        if num_2==target-num_1:
            flag=True
            num1=num_1
            num2=num_2
            break
    if flag==True:
        break
print(num1)
print(num2)
sol=num_1*num_2
print(sol)

