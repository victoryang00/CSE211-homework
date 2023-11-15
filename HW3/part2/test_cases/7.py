for i in range(7,10):
    for j in range(i,100):
        for k in range(0,j):
            for m in range(i,j):
                for q in range(10,100):
                    a[m*q+1] = a[k+i+j*q]
