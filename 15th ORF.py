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
st = strings[0]
st = st.replace('T', 'U')
print(st)
all_acs = []
acs = []
ac = {'UUU':'F', 'UUC':'F', 'UUA':'L', 'UUG':'L', 'UCU':'S', 'UCC':'S', 'UCA':'S', 'UCG':'S', 'UAU':'Y', 'UAC':'Y', 'UAA':'Stop', 'UAG':'Stop', 'UGU':'C', 'UGC':'C', 'UGA':'Stop', 'UGG':'W', 'CUU':'L', 'CUC':'L', 'CUA':'L', 'CUG':'L', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'CAU':'H', 'CAC':'H', 'CAA':'Q', 'CAG':'Q', 'CGU':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AUU':'I', 'AUC':'I', 'AUA':'I', 'AUG':'M', 'ACU':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T', 'AAU':'N', 'AAC':'N', 'AAA':'K', 'AAG':'K', 'AGU':'S', 'AGC':'S', 'AGA':'R', 'AGG':'R', 'GUU':'V', 'GUC':'V', 'GUA':'V', 'GUG':'V', 'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'GAU':'D', 'GAC':'D', 'GAA':'E', 'GAG':'E', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', }
for i in range(0, len(st)+1, 3):
    if i >= 3:
        c = 0
        if len(acs) == 0:
            co = st.index('AUG', c)
            for j in range(0, len(st)+1, 3):
                key = st[co+j-3:co+j]
                if len(key) != 3:
                    break
                if ac[key] == 'Stop':
                    c = co+j-3
                    all_acs.append(acs)
                    acs.clear()
                    break
                acs.append(ac[key])
                print(acs)
                print('c:', c)
            print('c:', c)
            print(co)
        '''if ac[key] == 'Stop':
            c = co+i-3
            all_acs.append(acs)
            acs.clear()
            continue
        acs.append(ac[key])'''
        print(ac[key])
        print(acs)
#print(''.join(acs))
print(all_acs)
        
    

