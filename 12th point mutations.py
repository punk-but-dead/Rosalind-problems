strings = []
names = []
data = list(iter(input, ''))
for i in range(len(data)):
    d = data[i]
    if d[0] == '>':
        d = d.replace('>', '')
        names.append(d)
    else:
        if '>' in data[i-1]:
            s = d
            #print('s.in:', s)
            for k in range(len(data)):
                g = data[k]
                if k-1 >= i:
                    if '>' in data[k]:
                        break
                    if g[0] != '>':
                        s += g
                        #print('s:', s)
                        if data[k] == data[-1]:
                            strings.append(s)
                            #print(strings)
                        elif k+1 < len(data):
                            if '>' in data[k+1]:
                                strings.append(s)
                                #print(strings)

print(strings)
first = strings[0]
second = strings[1]
purin = ['A', 'G']
purimidine = ['C', 'T']
transitions = 0
transversions = 0
for i in range(len(first)):
    if first[i] != second[i]:
        if first[i] in purin:
            if second[i] in purin:
                transitions += 1
            elif second[i] in purimidine:
                transversions += 1
        if first[i] in purimidine:
            if second[i] in purin:
                transversions += 1
            elif second[i] in purimidine:
                transitions += 1
print(transitions/transversions)
