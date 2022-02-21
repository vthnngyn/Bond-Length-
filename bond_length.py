import math
import numpy as np
import statistics 
from statistics import mean
from prettytable import PrettyTable

#xyz file to be read 
file = input ("File of xyz coordinates:")
a = np.genfromtxt(file, delimiter=None, dtype=('str'), unpack=True, usecols=[0])      
x, y, z = np.genfromtxt(file, delimiter=None, unpack=True, usecols=[1, 2, 3])

#index atoms to a number
N = len(a)
print("Number of atoms:", N)
a_list = list(a)
a_a = list(range(1,N+1))
atom_table = PrettyTable(['Atom', 'Atom Number'])
for m in range(0,N):
    atom_table.add_row([a_list[m], a_a[m]])
print(atom_table)

#choose an upper limit to define bond desired bonded length
L_input = input ("Upper limit for desired bond length (units defined by inputted file):")
L_float = float(L_input)
bond = []
coord = []
coordtwo = []
CN = []
bond_table = PrettyTable(['Atom', 'Bonded Atom', 'Atom Number', 'Bonded Atom Number', 'Bond Length'])
for i in range(0,N-1):
    for j in range(i+1,N-0):
        dx = x[j] - x[i]
        dy = y[j] - y[i]
        dz = z[j] - z[i]
        L = round(math.sqrt(dx**2 + dy**2 + dz**2),2)
        if L < L_float:                                                                      
             bond_table.add_row([a[i], a[j], a_a[i], a_a[j], L]) 
             bond.append(L)
             coord.append(a_a[i])
             coordtwo.append(a_a[j])
print(bond_table)
print("Average bond length is", round(mean(bond),2), "with standard deviation", round(statistics.stdev(bond),2))

#coordination number determined by counting the bonds for an atom to all other atoms that are under L 
coord_table = PrettyTable(['Atom', 'Atom Number', 'Coordination Number'])
for k in range(1,N+1):                                                                      
     coord_table.add_row([a[k-1], k, coord.count(k)+coordtwo.count(k)])
     CN.append(coord.count(k)+coordtwo.count(k))
print(coord_table)
print("Average coordination is", round(mean(CN),2), "with standard deviation", round(statistics.stdev(CN),2))
