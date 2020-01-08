import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if
r1=5
b=5
d=r1
e=np.sqrt(5**2-r1**2)
len = 50
B = np.array([0,0])
C = np.array([5,0])

#Coordinates of M & N
p1 = (b**2 + d**2-e**2 )/(2*b)
q1 = np.sqrt(d**2-p1**2)
A= np.array([p1,q1])
print(A)

O=np.array([0,0])

O1=np.array([5,0])

 
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O).T

#Generating all lines
x_BC = line_gen(B,C)
x_BA = line_gen(B,A)



plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')

#Plotting all line

plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_BA[0,:],x_BA[1,:],label='$BA$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')

plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 - 0.2), C[1] * (1) , 'C')

plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/circle/circumcircle.pdf')
#plt.savefig('./figs/circle/circumcircle.eps')
#subprocess.run(shlex.split("termux-open ./figs/circle/circumcircle.pdf"))
#else
plt.show()
