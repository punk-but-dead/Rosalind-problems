s = str(input())
s1 = ''
for i in range(len(s)):
    if s[i] == 'A':
        s1 += 'T'
    if s[i] == 'C':
        s1 += 'G'
    if s[i] == 'G':
        s1 += 'C'
    if s[i] == 'T':
        s1 += 'A'
print(s1[::-1])
