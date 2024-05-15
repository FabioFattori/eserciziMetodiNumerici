# rango massimo e matrice ben condizionata
import esercitazioniEsame.SolveTriangular as SolveTriangular
import numpy as np
import scipy.linalg as spLin
import matplotlib.pyplot as plt

def eqnorm(A,b):
 
    G=A.T@A
    condG=np.linalg.cond(G) 
    print("Indice di condizionamento di G ",condG)
    f=A.T@b
    
    L=spLin.cholesky(G,lower=True)
    U=L.T
        
   
    z,flag=SolveTriangular.Lsolve(L,f)
    if flag==0:
        x,flag=SolveTriangular.Usolve(U,z)
    
    
    return x

#Esempio di utilizzo
x = np.array([-3.5,  -3 , -2, -1.5, -0.5,  0.5,  1.7,  2.5, 3])
y = np.array([-3.9, -4.8, -3.3, -2.5,  0.3,  1.8,  4,  6.9,  7.1])
m=x.shape[0]
n=1
n1=n+1
A=np.vander(x,increasing=True)[:,:n1]

a_EQN=eqnorm(A,y)
print("a_EQN=",a_EQN)
xv=np.linspace(np.min(x),np.max(x),200)
pol_eqn=np.polyval(np.flip(a_EQN),xv) # flip because of the way np.polyval is defined , polyval vuole i coefficienti in ordine decrescente mentre noi li calciamo in ordine crescente
plt.plot(x,y,'*',xv,pol_eqn)
plt.title('Equazioni Normali')
plt.show()