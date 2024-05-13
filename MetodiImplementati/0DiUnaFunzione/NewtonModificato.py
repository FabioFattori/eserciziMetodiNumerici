def newtonModificato(f,fp,m,x0,tolf,tolx,maxIt):
    '''
    INPUT:
    f: lambda, funzione
    fp: lambda, derivata della funzione
    m: float, molteplicità dello zero
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
    while it<maxIt and abs(f(x0))>tolf and abs(fp(x0))>tolx:
        x1=x0-m*f(x0)/fp(x0)
        x_k.append(x1)
        it+=1
        if f(x1)==0:
            return [x1, it, x_k]
        x0=x1
    return [x0, it, x_k]