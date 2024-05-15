import numpy as np
import scipy.linalg as spLin
import matplotlib.pyplot as plt

#matrice molto mal condizionata => sta troia , il rango può anche essere non massimo 
def svdsolve(A,b):
    m,n=A.shape  #numero di righe e  numero di colonne di A
    U,s,VT=spLin.svd(A)  #Attenzione : Restituisce U, il numpy-array 1d che contiene la diagonale della matrice Sigma e VT=VTrasposta)
    #Quindi 
    V=VT.T
    thresh=np.spacing(1)*m*s[0] ##Calcolo del rango della matrice, numero dei valori singolari maggiori di una soglia
    k=np.count_nonzero(s>thresh)
    print("rango=",k)
    d=U.T@b
    d1=d[:k].reshape(k,1)
    s1=s[:k].reshape(k,1)
    #Risolve il sistema diagonale di dimensione kxk avene come matrice dei coefficienti la matrice Sigma
    c=d1/s1
    x=V[:,:k]@c 
    residuo=np.linalg.norm(d[k:])**2
    return x,residuo


# esempio di utilizzo
x = np.array([1.001, 1.004, 1.005,1.0012,1.0013, 1.0014, 1.0015, 1.0016]) 
y = np.array([-1.2, -0.95, -0.9, -1.15, -1.1, -1])
m=x.shape[0]
n=1
n1=n+1
A_3=np.vander(x,increasing=True)[:,:n1]
res,residuo=svdsolve(A_3,y)
print("res=",res)
xv=np.linspace(np.min(x),np.max(x),200)
pol_eqn=np.polyval(np.flip(res),xv)
plt.plot(x,y,'*',xv,pol_eqn)
plt.title('svdsolve')
plt.show()