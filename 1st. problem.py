s = str(input())
lens = []
for n in ['A', 'C', 'G', 'T']:
    lens.append(s.count(n))
print(*lens)
