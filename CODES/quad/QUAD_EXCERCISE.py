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
x=2.5
y=6
z=6

print(c)

#Coordinates of D
p = (a**2 + c**2-b**2 )/(2*a)
q = np.sqrt(c**2-p**2)
print(p,q)



#Parallelogram vertices
D = np.array([p,q]) 
B = np.array([0,0]) 
C = np.array([a,0]) 

#Mid point of BD
O =(B+D)/2


#Finding A
A = 2*O-C
F = (A+D)/2


#Triangle vertices
BFC= tri_vert(a,b,c)
G =  alt_foot(F,B,C)
ABF= tri_vert(a,b,c)
T =  alt_foot(A,B,F)

#Normal vectors of AD and BE
n1 = B-C
n1 = A-F




print(D)
#Generating all lines
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_FB = line_gen(F,B)
x_FC = line_gen(F,C)
x_FG = line_gen(F,G)


x_AD = line_gen(A,D)
x_CD = line_gen(C,D)

#Plotting all lines
plt.plot(x_AB[0,:],x_AB[1,:],label='$AB$')
plt.plot(x_BC[0,:],x_BC[1,:],label='$BC$')
plt.plot(x_FC[0,:],x_FC[1,:],label='$FC$')
plt.plot(x_FB[0,:],x_FB[1,:],label='$FB$')
plt.plot(x_FG[0,:],x_FG[1,:],label='$FG$')
plt.plot(x_AD[0,:],x_AD[1,:],label='$AD$')
plt.plot(x_CD[0,:],x_CD[1,:],label='$CD$')

plt.plot(A[0], A[1], 'o')
plt.text(A[0] * (1 + 0.1), A[1] * (1 - 0.1) , 'A')
plt.plot(B[0], B[1], 'o')
plt.text(B[0] * (1 - 0.2), B[1] * (1) , 'B')
plt.plot(C[0], C[1], 'o')
plt.text(C[0] * (1 + 0.03), C[1] * (1 - 0.1) , 'C')
plt.plot(D[0], D[1], 'o')
plt.text(D[0] * (1 + 0.03), D[1] * (1 - 0.1) , 'D')
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
#plt.savefig('./figs/quad/pgm_sss.pdf')
#plt.savefig('./figs/quad/pgm_sss.eps')
#subprocess.run(shlex.split("termux-open ./figs/quad/pgm_sss.pdf"))
#else
plt.show()




