import numpy as np
import matplotlib.pyplot as plt
from coeffs import *
#from circumcentre import  ccircle
#if using termux
#import subprocess
#import shlex
#end if


len = 50
r1 = 4
a=2
c=4
b=np.sqrt(c**2-a**2)
print(b)


S = np.array([-a,b]) 
R = np.array([a,b]) 
O=np.array([0,0])
Q=np.array([a,-b])
P = np.array([-a,-b]) 


theta = np.linspace(0,2*np.pi,len)
x_circ1 = np.zeros((2,len))
x_circ1[0,:] = r1*np.cos(theta)
x_circ1[1,:] = r1*np.sin(theta)
x_circ1 = (x_circ1.T + O).T
#Generating all lines
x_SR = line_gen(S,R)
x_QP = line_gen(Q,P)
x_SP = line_gen(S,P)
x_RQ = line_gen(R,Q)
plt.plot(x_circ1[0,:],x_circ1[1,:],label='$circle1$')



#Plotting all lines
plt.plot(x_SR[0,:],x_SR[1,:],label='$SR$')
plt.plot(x_QP[0,:],x_QP[1,:],label='$QP$')
plt.plot(x_SP[0,:],x_SP[1,:],label='$SP$')
plt.plot(x_RQ[0,:],x_RQ[1,:],label='$RQ$')
plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P(-2,-3.46)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q(2,-3.46)')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.1) , 'R(2,3.36)')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.1) , 'S(-2,3.46)')

plt.plot(O[0], O[1], 'o')
plt.text(O[0] * (1 + 0.03), O[1] * (1 - 0.1) , 'O')

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
