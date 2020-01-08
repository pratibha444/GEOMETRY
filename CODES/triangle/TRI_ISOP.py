import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
#a = 6
a = 6.5
c = 6.5
angA = 110*np.pi/180
b = np.sqrt(a**2+c**2 - 2*a*c*np.cos(angA))
print(b)
#Coordinates of A
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 
P = np.array([1,-2.2]) 
Q = np.array([9.2,-2]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CA = line_gen(C,A)
x_BP = line_gen(B,P)
x_CQ = line_gen(C,Q)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_CA[0,:],x_CA[1,:],label='$CA$')
plt.plot(x_BP[0,:],x_BP[1,:],label='$BP$')
plt.plot(x_CQ[0,:],x_CQ[1,:],label='$CQ$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.01) , 'A(-2.22,6.10)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(0,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (0.5 - 0.1) , 'C(6.5,0)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.2), P[1] * (1) , 'P(1,-2.2)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 + 0.03), Q[1] * (0.5 - 0.1) , 'Q(9.2,-2)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/triangle/tri_sss.pdf')
plt.savefig('../../figs/NEWTRI.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_sss.pdf"))
#else
plt.show()






