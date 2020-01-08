import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if
r1=4
r2=6
a=np.sqrt(6**2-r1**2)
c=r1
b=r2
print(a)

len = 50
A = np.array([0,0])
B = np.array([r2,0])

#Coordinates of P & Q
p = (b**2 + c**2-a**2 )/(2*b)
q = np.sqrt(c**2-p**2)
P= np.array([p,q])
Q= np.array([p,-q])


O=np.array([0,0])
print(P)
print(Q)


 
theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O).T

x_circ2 = np.zeros((2,len))
x_circ2[0,:] = r2*np.cos(theta)
x_circ2[1,:] = r2*np.sin(theta)
x_circ2 = (x_circ2.T + O).T
#Generating all lines
x_AB = line_gen(A,B)
x_AP = line_gen(A,P)
x_PB = line_gen(P,B)
x_QB = line_gen(Q,B)
x_AQ = line_gen(A,Q)

plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')
plt.plot(x_circ2[0,:],x_circ2[1,:],label='$circle1$')

#Plotting all line

plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_PB[0,:],x_PB[1,:],label='$PB$')
plt.plot(x_QB[0,:],x_QB[1,:],label='$QB$')
plt.plot(x_AQ[0,:],x_AQ[1,:],label='$AQ$')


plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A(0,0)')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B(6,0)')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 - 0.2), P[1] * (1) , 'P(2.66,2.98)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q(2.66,-2.98)')


plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='upper right')
plt.grid() # minor
plt.axis('equal')
plt.savefig('../../figs/CIR_CON.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else

plt.show()
