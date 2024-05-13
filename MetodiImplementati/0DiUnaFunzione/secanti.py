def secanti(x1,x0,f,tolx,tolf,maxIt):
    '''
    Calcolo dello zero di una funzione tramite il metodo delle secanti, restituisco lo zero , il numero di iterazioni e i valori di x calcolati
    INPUT:
    x1: float, secondo punto iniziale
    x0: float, punto iniziale
    f: lambda, funzione
    tolx: float, tolleranza richiesta
    tolf: float, tolleranza della funzione richiesta
    maxIt: int, numero massimo di iterazioni

    OUTPUT:
    [0] => 0 della funzione
    [1] => numero di iterazioni
    [2] => valore di x
    '''
    xk=[]
    fxm1=f(xm1)
    fx0=f(x0) 
    d=fx0*(x0-xm1)/(fx0-fxm1)
    x1=x0-d
    xk.append(x1)
    fx1=f(x1)
    it=1
    while it<maxIt and abs(fx1)>=tolf and abs(d)>=tolx*abs(x1):
        xm1=x0
        x0=x1
        fxm1=f(xm1)
        fx0=f(x0) 
        d=fx0*(x0-xm1)/(fx0-fxm1)
        x1=x0-d
        fx1=f(x1)
        xk.append(x1)
        it=it+1
       
    if it==maxIt:
       print('Secanti: raggiunto massimo numero di iterazioni \n')
    
    return [x1,it,xk]