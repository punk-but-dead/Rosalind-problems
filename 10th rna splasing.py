data = list(iter(input, ''))
#print(data)

for i in range(len(data)):
    if i < len(data):
        d = data[i]
        if i == 1:
            for k in range(len(data)):
                if k-1 >= i:
                    g = data[1]
                    if '>' in data[1]:
                        break
                    if g[0] != '>':
                        data[0] += g
                        data.pop(1)
                        print('0:', data[0])
        if d[0] == '>':
            data.pop(i)
#print(data)
for i in range(len(data[0])):
    if i < len(data) and i != 0:
        data[0] = data[0].replace(data[i], 'q', 1)
        print(data[0])
        if i+1 == len(data):
            data[0] = data[0].replace('q', '', -1)
            data[0] = data[0].replace('T', 'U', -1)
            string = data[0]
            print(string)
        
acs = []
ac = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', }
for i in range(0, len(string)+1, 3):
    if i >= 3:
        key = string[i-3:i]
        acs.append(ac[key])
        #print(ac[key])
acs.pop()
print(''.join(acs))
        
    
