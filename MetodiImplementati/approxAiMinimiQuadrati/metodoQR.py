import numpy as np
import scipy.linalg as spLin
import matplotlib.pyplot as plt
import esercitazioniEsame.SolveTriangular as SolveTriangular
#rango massimo e matrice mal(mediamente boh che cazzo vuol dire porco dio) condizionata
def QRsolve(A,b):
    n=A.shape[1]  # numero di colonne di A
    Q,R=spLin.qr(A)
    h=Q.T@b
    x,flag=SolveTriangular.Usolve(R[0:n,:],h[0:n])
    residuo=np.linalg.norm(h[n:])**2
    return x,residuo


# esempio di utilizzo
x2=np.array([0.0004,0.2507,0.5008,2.0007, 8.0013])
y2=np.array([0.0007,0.0162,0.0288, 0.0309,0.0310])
n=2 #parabola di regressione: grado 2 || se vuoi la retta di regressione metti n=1
n1=n+1  # gradi di libertà
A2=np.vander(x2,increasing=True)[:,:n1]
condA2=np.linalg.cond(A2)
print("condizionamento di A2 ",condA2)
#Poichè la matrice è mediamente ben condizionata (Ha un indice di condizionamento pari a  65.67493525624782
# (quinfi A.T@A avrà indice di condizionamento pari al quadrato dell'indice di condionamento di A)
#è quindi preferibile usare il metodo QR
alpha2,residuo_QR=QRsolve(A2,y2)
xv=np.linspace(np.min(x2),np.max(x2),100)
pol2=np.polyval(np.flip(alpha2),xv)
plt.plot(xv,pol2,x2,y2,'ro')
plt.show()
print("residuo ",residuo_QR)