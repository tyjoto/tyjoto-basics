import numpy as np

def first(x,y):
    """
    Second order first derivative
    """
    lenx = len(x)
    ders = np.zeros(lenx)
    for k in range(lenx):
        if k == 0:  # forward diff
            num = -y[k+2] + 4*y[k+1] - 3*y[k]
            den = ( x[k+2]-x[k] )
            der = np.divide(num,den)
        elif k == lenx-1:   # backward diff
            num = y[k-2] - 4*y[k-1] + 3*y[k]
            den =( -x[k-2]+x[k] )
            der = np.divide(num,den)
        else:   # central diff
            num = y[k+1] - y[k-1]
            den = ( x[k+1]-x[k-1] )
            der = np.divide(num,den)
        ders[k] = der
    return ders

def second(x,y):
    """
    Second order second derivative
    note fix forward and back
    """
    lenx = len(x)
    ders = np.zeros(lenx)
    for k in range(lenx):
        if k == 0:
            num = -y[k+3] + 4*y[k+2] - 5*y[k+1] + 2*y[k]
            den = np.multiply( x[k+1]-x[k] , \
                    x[k+3]-x[k+2])
            der = np.divide(num,den)
        elif k == lenx-1:
            num = y[k-3] - 4*y[k-2] + 5*y[k-1] - 2*y[k]
            den = np.multiply( x[k-1]-x[k] , \
                    -x[k-3]+x[k-2])
            der = np.divide(num,den)
        else:
            num = ( (y[k+1]-y[k])/(x[k+1]-x[k]) )\
                    -\
                    ( (y[k]-y[k-1])/(x[k]-x[k-1]) )
            den = ( (x[k+1]+x[k])/2 - (x[k]+x[k-1])/2 )
            der = np.divide(num,den)
        ders[k] = der
    return ders
def OLDsecond(x,y):
    """
    Second order second derivative
    """
    lenx = len(x)
    ders = np.zeros(lenx)
    for k in range(lenx):
        if k == 0:
            num = -y[k+3] + 4*y[k+2] - 5*y[k+1] + 2*y[k]
            den = np.multiply( x[k+1]-x[k] , \
                    x[k+3]-x[k+2])
            der = np.divide(num,den)
        elif k == lenx-1:
            num = y[k-3] - 4*y[k-2] + 5*y[k-1] - 2*y[k]
            den = np.multiply( x[k-1]-x[k] , \
                    -x[k-3]+x[k-2])
            der = np.divide(num,den)
        else:
            num = y[k+1] - 2*y[k] + y[k-1]
            den = np.multiply( x[k+1]-x[k], x[k]-x[k-1] )
            der = np.divide(num,den)
        ders[k] = der
    return ders
