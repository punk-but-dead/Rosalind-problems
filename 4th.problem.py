s = str(input())
t = str(input())
same = []
for i in range(len(s)):
    if t[i] == s[i]:
        same.append(s[i])
#print(len(same))
print(len(s) - len(same))
