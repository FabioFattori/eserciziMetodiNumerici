def corde(f,m,x0,tolx,tolf,maxIt):
    '''
    Calcolo dello zero di una funzione tramite il metodo delle corde, restituisco lo zero , il numero di iterazioni e i valori di x calcolati
    INPUT:
    f: lambda, funzione
    m: float, coefficente angolare della retta => (f(b)-f(a))/(b-a)
    x0: float, punto iniziale
    tolx: float, tolleranza richiesta
    tolf: float, tolleranza della funzione richiesta
    maxIt: int, numero massimo di iterazioni

    OUTPUT:
    [0] => 0 della funzione
    [1] => numero di iterazioni
    [2] => valore di x 
    '''
    it=1
    x_k=[]
    x_k.append(x0)
    if f(x0)==0:
        return [x0, it, x_k]
    while it<maxIt and abs(f(x0))>tolf and abs(m-f(x0)/m)>tolx:
        x1=x0-f(x0)/m
        x_k.append(x1)
        it+=1
        if f(x1)==0:
            return [x1, it, x_k]
        x0=x1
    return [x0, it, x_k]