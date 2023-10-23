strings = []
proc = []
names = []
ind = []
data = list(iter(input, ''))
#print(data)
#print(strings)
#print(names)
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
                    
#print(data)
#print('strings:', strings)
#print(names)
for i in range(len(strings)):
    c = strings[i].count('C') + strings[i].count('G')
    proc.append(c/len(strings[i]))
n = proc.index(max(proc))
print(names[n])
print(max(proc)*100)
#print(strings)
    
    
        
        
        
        
        
