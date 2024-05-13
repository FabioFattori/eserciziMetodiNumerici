import sign
def falsi(a,b,f,tol,maxIterations):
    '''
    Calcolo dello zero di una funzione tramite il metodo dei falsi , restituisco lo zero , il numero di iterazioni e i valori di x calcolati
    INPUT:
    a: float, estremo sinistro dell'intervallo
    b: float, estremo destro dell'intervallo
    f: lambda, nome della funzione
    tol: float, tolleranza da non superare => calcolata tramite np.abs(maxIntervallo-minIntervallo) > tolleranza
    maxIterations: int, numero massimo di iterazioni

    OUTPUT:
    [0] => 0 della funzione
    [1] => numero di iterazioni
    [2] => valore di x 
    '''
    fa=f(a)
    fb=f(b)
    if sign(fa)*sign(fb) >= 0:
         # throw error
        print("f(a) e f(b) hanno lo stesso segno",fa,fb)    
    it = 0
    x_k=[]
    c=0.0
    fxk=10
    while abs(b-a) > tol and it < maxIterations and abs(fxk) > tol:
        c = a-f(a)*(b-a)/(f(b)-f(a))
        x_k.append(c)
        fxk=f(c)
        it+=1
        if f(c) == 0:
            return [c, it, x_k]
        if f(a)*f(c) < 0:
            b = c
        else:
            a = c
    return [c, it, x_k]