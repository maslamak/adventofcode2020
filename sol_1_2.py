fname='input_1.txt'
f = open(fname)
nums = f.readlines()
nums = [int(i) for i in nums]
target = 2020
flag = False
for ind_1, num_1 in enumerate(nums):
    for ind_2 in range(ind_1, len(nums)):
        num_2 = nums[ind_2]
        for ind_3 in range(ind_2 + 1, len(nums)):
            num_3 = nums[ind_3]
            if num_1 + num_2 + num_3 == target:
                flag = True
                num1 = num_1
                num2 = num_2
                num3 = num_3
                break
        if flag:
            break
    if flag:
        break
print(num1)
print(num2)
print(num3)
sol = num1 * num2 * num3
print(sol)
