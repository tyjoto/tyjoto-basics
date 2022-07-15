import numpy as np

def unpack(data):
    """
    data: Must be a numpy array with pairs in a row
    i.e.    x1,y1
            x2,y2
    returns: x,xerr,y,yerr
    """
    # get data shape (numpy)
    shape_data = data.shape
    lendatax = shape_data[0]
    lendatay = shape_data[1]
    # if err is part of data
    if lendatay == 4:
        x = data[:,0];  xerr = data[:,1]
        y = data[:,2];  yerr = data[:,3]
    elif lendatay == 2:
        x = data[:,0];  xerr = None
        y = data[:,2];  yerr = None
    else:
        print("Unknown if error is provided for x or y")
    return x,xerr,y,yerr

def reorder(x,y,/,xerr=None,yerr=None):
    l = 2
    if xerr is not None: l = l+1
    if yerr is not None: l = l+1
    data = [None]*l
    k = 1
    sorted_zipped_lists = sorted(zip(x,y))
    Y = [element for _, element in sorted_zipped_lists]
    data[k] = Y
    k = k+1
    if xerr is not None:
        sorted_zipped_lists_2 = sorted(zip(x,xerr))
        Xerr = [element for _, element in sorted_zipped_lists_2]
        data[k] = Xerr
        k = k+1
    else:
        Xerr = None
    if yerr is not None:
        sorted_zipped_lists_3 = sorted(zip(x,yerr))
        Yerr = [element for _, element in sorted_zipped_lists_3]
        data[k] = Yerr
        k = k+1
    else:
        Yerr = None

    X = sorted(x)
    data[0] = X
    return X,Xerr,Y,Yerr

def repack(x,y,/,xerr=None,yerr=None):
    l = 2
    if xerr is not None: l = l+1
    if yerr is not None: l = l+1
    cols = l
    rows = len(x)
    data = np.zeros([rows,cols])
    k = 1
    for k in range(l):
        if k==0:
            data[:,0] = x
        if xerr is not None and yerr is not None:
            if k==1:
                data[:,k] = xerr
            elif k==2:
                data[:,k] = y
            elif k==3:
                data[:,k] = yerr
            elif k==0:
                pass
            else:
                print("ERROR1")
        elif xerr is None and yerr is None:
            if k==1:
                data[:,k] = y
            elif k==0:
                pass
            else:
                print("ERROR2")
        elif xerr is not None and yerr is None:
            if k==1:
                data[:,k] = xerr
            elif k==2:
                data[:,k] = y
            elif k==0:
                pass
            else:
                print("ERROR3")
        elif xerr is None and yerr is not None:
            if k==1:
                data[:,k] = y
            elif k==2:
                data[:,k] = yerr
            elif k==0:
                pass
            else:
                print("ERROR4")
        else:
            print("ERROR0")
    return data





