import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
import subprocess
import shlex
#end if


#Triangle sides
#a = 6
r=14
len=50

c = r
a = r
angA = 30*np.pi/180
b =  np.sqrt(a**2+c**2 - 2*a*c*np.cos(angA))
print(b)
#Coordinates of A
#p = (a**2 + c**2-b**2 )/(2*a)
#q = np.sqrt(c**2-p**2)
#print(p,q)

O=np.array([0,0])

 
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r*np.cos(theta)
x_circ1[1,:] = r*np.sin(theta)
x_circ1 = (x_circ1.T + O).T


theta=np.pi/180*(30)
p=r*np.cos(theta)
q=r*np.sin(theta)
print(p,q)
#Triangle vertices
A = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 

#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)

plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')


#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(12.12,6.99)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(0,0)')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C(14,0)')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/triangle/tri_sss.pdf')
plt.savefig('../../figs/miscp.eps')
#subprocess.run(shlex.split("termux-open ./figs/triangle/tri_sss.pdf"))
#else
plt.show()






