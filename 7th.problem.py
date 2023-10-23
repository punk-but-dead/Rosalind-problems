k = int(input()) #dominant
m = int(input()) #heterozigotis
n = int(input()) #recessive
s = k + n + m
doms = []
Ck = k*(k-1)//2
Cm = m*(m-1)//2
Cn = n*(n-1)//2
doms.append(4*Ck) #
doms.append(4*k*m)
doms.append(4*k*n)
doms.append(n*m*2)
doms.append(Cm*3)
print(doms)
a = doms[0] + doms[1] + doms[2] + doms[3] + doms[4]
print(round(a/(2*(s*(s-1))), 5))
