import itertools
n = int(input())
nums = []
for i in range(n):
    nums.append(i+1)
#print(nums)
arr = list(itertools.permutations(nums))
print(len(arr))
#print(arr)
for i in range(len(arr)):
    #print(arr[i])
    s = str(arr[i])
    
    s = s.replace('(', '')
    s = s.replace(')', '')
    s = s.replace(',', '')
    print(s)
