import numpy as np

def bisezione(minIntervallo,maxIntervallo,fname,tolleranza,nInterazioniMax):
    '''
    Calcolo dello zero di una funzione tramite il metodo della bisezione, restituisco lo zero , il numero di iterazioni e i valori di x calcolati
    INPUT:
    minIntervallo: float, estremo sinistro dell'intervallo
    maxIntervallo: float, estremo destro dell'intervallo
    fname: lambda, nome della funzione
    tolleranza: float, tolleranza da non superare => calcolata tramite np.abs(maxIntervallo-minIntervallo) > tolleranza
    nInterazioniMax: int, numero massimo di iterazioni

    OUTPUT:
    [0] => 0 della funzione
    [1] => numero di iterazioni
    [2] => valore di x 
    '''
    if fname(minIntervallo)*fname(maxIntervallo) >= 0:
        print("Non ci sono zeri nell'intervallo")
        return None,None,None
    
    nInterazioni=0
    valoriXCalcolati = np.empty(0)
    x = None

    while np.abs(maxIntervallo-minIntervallo) > tolleranza and nInterazioni < nInterazioniMax:
        nInterazioni+=1
        x = (maxIntervallo-minIntervallo)/2 + minIntervallo
        valoriXCalcolati = np.append(valoriXCalcolati,x)
        if fname(x) == 0:
            return x,nInterazioni,valoriXCalcolati
        elif fname(minIntervallo)*fname(x) < 0:
            maxIntervallo = x
        else:
            minIntervallo = x
    
    if nInterazioni < nInterazioniMax and np.abs(maxIntervallo-minIntervallo) < tolleranza:
        print("tolleranza superata")

    return x,nInterazioni,valoriXCalcolati
    
