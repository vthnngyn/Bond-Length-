import math
import numpy as np
import statistics 
from statistics import mean

#xyz file to be read 
a = np.genfromtxt('coords.xyz', delimiter=None, dtype=('str'), unpack=True, usecols=[0])      
x, y, z = np.genfromtxt('coords.xyz', delimiter=None, unpack=True, usecols=[1, 2, 3])

N = len(a)
print(N)
a_a = list(range(1,N+1))
print(a_a)
bond = []
coord = []
coordtwo = []
CN = []

for i in range(0,N-1):
    for j in range(i+1,N-0):
        dx = x[j] - x[i]
        dy = y[j] - y[i]
        dz = z[j] - z[i]
        L = round(math.sqrt(dx**2 + dy**2 + dz**2),2)
        #desired upper limit for bond length L
        if L < int(3):                                                                      
             print(a[i],a[j],a_a[i],a_a[j],L) 
             bond.append(L)
             coord.append(a_a[i])
             coordtwo.append(a_a[j])

print("Average bond length is", round(mean(bond),2))
print("Standard deviation is", round(statistics.stdev(bond),2))

#coordination number determined by counting the bonds for an atom to all other atoms that are under L 
for i in range(1,N+1):                                                                      
     print(a[i-1],i,coord.count(i)+coordtwo.count(i))
     if coord.count(i)+coordtwo.count(i) < int(12):    
          CN.append(coord.count(i)+coordtwo.count(i))

print("Average coordination is", round(mean(CN),2))
print("Standard deviation is", round(statistics.stdev(CN),2))
     


