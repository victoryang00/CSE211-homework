for i in range(7,10):
    for j in range(i,100):
        for k in range(0,j):
            a[i*j*k] = a[k*5]
