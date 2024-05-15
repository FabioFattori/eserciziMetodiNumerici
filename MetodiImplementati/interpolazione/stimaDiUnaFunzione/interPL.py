import numpy as np
def plagr(xnodi,j):
    """
    Restituisce i coefficienti del j-esimo pol di
    Lagrange associato ai punti del vettore xnodi
    """
    xzeri=np.zeros_like(xnodi)
    n=xnodi.size
    if j==0:
       xzeri=xnodi[1:n]
    else:
       xzeri=np.append(xnodi[0:j],xnodi[j+1:n])
    
    num=np.poly(xzeri)
    den=np.polyval(num,xnodi[j])
    
    p=num/den
    
    return p

def InterpL(x, y, xx):
     """"
        %funzione che determina in un insieme di punti il valore del polinomio
        %interpolante ottenuto dalla formula di Lagrange.
        % DATI INPUT
        %  x  vettore con i nodi dell'interpolazione
        %  f  vettore con i valori dei nodi 
        %  xx vettore con i punti in cui si vuole calcolare il polinomio
        % DATI OUTPUT
        %  y vettore contenente i valori assunti dal polinomio interpolante
        %
     """
     n=x.size
     m=xx.size
     L=np.zeros((m,n))
     for j in range(n):
        p=plagr(x,j)
        L[:,j]=np.polyval(p,xx)
    
    
     return L@y

# Esempio di utilizzo
import math
import matplotlib.pyplot as plt
k=np.arange(0,5,1)
x = k*math.pi/2
y=np.sin(x)
xx=np.linspace(0,2*math.pi,100)

yy=InterpL(x,y,xx)
plt.plot(xx,yy)
plt.plot(x,y,'*')
plt.plot(xx,np.sin(xx),"--")
plt.legend(['Interpolazione','Nodi','sin(x)'])
plt.title('Interpolazione con polinomi di Lagrange')
plt.show()