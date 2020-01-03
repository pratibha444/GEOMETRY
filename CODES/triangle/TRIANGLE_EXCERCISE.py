import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
#a = 6
b = 4
c = 4
angA = 70*np.pi/180
a = np.sqrt(b**2+c**2 - 2*b*c*np.cos(angA))
print(a)
f=-1
g=5.3
#Coordinates of A
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 
F = np.array([-0.8,f]) 
G = np.array([g,f]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_BF = line_gen(B,F)
x_CG = line_gen(C,G)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_BF[0,:],x_BF[1,:],label='$BF$')
plt.plot(x_CG[0,:],x_CG[1,:],label='$CG$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(F[0], F[1], 'o')
plt.text(F[0] * (1 + 0.03), F[1] * (1 - 0.1) , 'F')
plt.plot(G[0], G[1], 'o')
plt.text(G[0] * (1 + 0.03), G[1] * (1 - 0.1) , 'G')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/triangle/tri_sss.pdf')
#plt.savefig('./figs/triangle/tri_sss.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_sss.pdf"))
#else
plt.show()






