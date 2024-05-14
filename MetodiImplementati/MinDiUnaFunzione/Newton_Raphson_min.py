import numpy as np
def Newton_Raphson_Minimo(gradF,hessF,X0,tolx,tolf,maxIt):
    '''
    metodo di Newton-Raphson per il calcolo del minimo di una funzione scalare. 
    input:
    - gradF: nome della funzione che calcola il gradiente della funzione scalare;
    - hessF: nome della funzione che calcola l'hesseiana della funzione scalare;
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
    grad_k=gradF(X0)
    hess_k=hessF(X0)
    if np.linalg.det(hess_k) == 0:
        print("La matrice dello Jacobiano calcolata nell'iterato precedente non è a rango massimo")
        return None, None,None
    X1=X0-np.linalg.solve(hess_k,grad_k)
    X_k.append(X1)
    while it<maxIt and np.linalg.norm(X1-X0)/np.linalg.norm(X0)>tolx and np.linalg.norm(grad_k)>tolf:
        X0=X1
        grad_k=gradF(X0)
        hess_k=hessF(X0)
        X1=X0-np.linalg.solve(hess_k,grad_k)
        X_k.append(X1)
        it+=1
    return [X1, it, X_k]