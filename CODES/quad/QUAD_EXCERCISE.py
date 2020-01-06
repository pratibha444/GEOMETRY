import numpy as np
import matplotlib.pyplot as plt
from coeffs import *


#if using termux
#import subprocess
#import shlex
#end if


#Triangle sides
#a = 6
#b = 4.5
#c = 7.5
a = 5
b = 6
angD = np.pi/180*85
c = np.sqrt(a**2+b**2-2*a*b*np.cos(angD))


print(c)

#Coordinates of D
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)



#Parallelogram vertices
R = np.array([p,q]) 
P = np.array([0,0]) 
Q = np.array([a,0]) 

#Mid point of BD
O =(P+R)/2


#Finding A
S = 2*O-Q
print(S)
A = (S+R)/2
print(A)


#Triangle vertices
PAQ= tri_vert(a,b,c)
G =  alt_foot(A,P,Q)
print(G)


#Normal vectors of AD and BE
n1 = P-Q





print(R)
#Generating all lines
x_SP = line_gen(S,P)
x_PQ = line_gen(P,Q)
x_QR = line_gen(Q,R)
x_RS = line_gen(R,S)
x_AP = line_gen(A,P)


x_AQ = line_gen(A,Q)
x_AG = line_gen(A,G)

#Plotting all lines
plt.plot(x_SP[0,:],x_SP[1,:],label='$SP$')
plt.plot(x_PQ[0,:],x_PQ[1,:],label='$PQ$')
plt.plot(x_QR[0,:],x_QR[1,:],label='$QR$')
plt.plot(x_RS[0,:],x_RS[1,:],label='$RS$')
plt.plot(x_AP[0,:],x_AP[1,:],label='$AP$')
plt.plot(x_AQ[0,:],x_AQ[1,:],label='$AQ$')
plt.plot(x_AG[0,:],x_AG[1,:],label='$AG$')

plt.plot(P[0], P[1], 'o')
plt.text(P[0] * (1 + 0.1), P[1] * (1 - 0.1) , 'P(0,0)')
plt.plot(Q[0], Q[1], 'o')
plt.text(Q[0] * (1 - 0.2), Q[1] * (1) , 'Q(5,0)')
plt.plot(R[0], R[1], 'o')
plt.text(R[0] * (1 + 0.03), R[1] * (1 - 0.05) , 'R(4.477,5.97)')
plt.plot(S[0], S[1], 'o')
plt.text(S[0] * (1 + 0.03), S[1] * (1 - 0.05) , 'S(-0.52,5.97)')
plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.03), A[1] * (1 - 0.03) , 'A(1.977,5.977)')
plt.plot(G[0], G[1], 'o')
plt.text(G[0] * (1 + 0.03), G[1] * (1 - 0.1) , 'G(1.977,0)')



plt.xlabel('$x$')
plt.ylabel('$y$')
plt.legend(loc='best')
plt.grid() # minor
plt.axis('equal')

#if using termux
#plt.savefig('./figs/quad/pgm_sss.pdf')
#plt.savefig('./figs/quad/pgm_sss.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else
plt.show()




