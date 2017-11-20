import decimal
m,p,q = map(int,input().split())
m1 = m
m2 = m1 - (m1 * (p*0.01))
m3 = m2 - (m2 * (q*0.01))
m4 = m3
print("{:.4f}".format(m4))
