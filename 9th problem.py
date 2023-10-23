nums = str(input())
nums = nums.split(' ')
#print(nums)
numbers = []
for i in range(len(nums)):
    s = int(nums[i])
    numbers.append(s)
print(numbers)
amount = 0
reproductive = 0
new = []
for i in range(numbers[0]-1):
    if i == 0:
        r = 1
        reproductive += 1
        #print('am:', amount)
    if i != 0:
        r = reproductive*numbers[1]
        new.append(r)
        #print('new:', new)
        if len(new) >= 2:
            reproductive += new[-2]
    #print('rep:', reproductive)
amount = sum(new) + 1
print(amount)
