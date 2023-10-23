s = str(input())
t = str(input())
for i in range(len(s)):
    if t in s[i:i+len(t)]:
        print(i+1)
