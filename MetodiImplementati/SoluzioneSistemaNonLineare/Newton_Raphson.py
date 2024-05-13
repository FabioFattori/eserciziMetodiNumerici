import numpy as np
def Newton_Raphson(f,j,X0,tolx,tolf,maxIt):
    '''
    metodo di Newton-Raphson per il calcolo della soluzione di un sistema di equazioni non lineari. 
    input:
    - f: nome della funzione vettoriale di cui calcolare lo zero;
    - j: nome della funzione che calcola lo J acobiano della funzione vettoriale;
    - X0: vettore contenente le componenti dell'iterato iniziale);
    - tolx tolleranza  per il test d'arresto sull'incremento
            ||X_{k+1}-X_k||/||X_{k}||<= tolx
    - tolf tolleranza per il test del residuo
            ||F(Xk+1)|| <= tolf;
    - maxIt numero massimo di iterazioni.
    In output devono essere restituiti il vettore contenente l'approssimazione dello zero x, un vettore contenente l'errore relativo tra due iterati successivi, il numero di iterazioni
    effettuate.
    '''
    it=1
    X_k=[]
    X_k.append(X0)
    F_k=f(X0)
    J_k=j(X0)
    if np.linalg.det(J_k) == 0:
        print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
        return None, None,None
    X1=X0-np.linalg.solve(J_k,F_k)
    X_k.append(X1)
    while it<maxIt and np.linalg.norm(X1-X0)/np.linalg.norm(X0)>tolx and np.linalg.norm(F_k)>tolf:
        X0=X1
        F_k=f(X0)
        J_k=j(X0)
        X1=X0-np.linalg.solve(J_k,F_k)
        X_k.append(X1)
        it+=1
    return [X1, it, X_k]