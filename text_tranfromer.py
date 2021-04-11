"""
    Transfrom data from CSV like to a python array
"""
def max_mem(name,header=False):
    print(name)
    max_elem = [['',0],['',0],['',0]]
    a = open(name,"r+").readlines()
    a = [i.replace("\n","") for i in a]
    a = [i.split(",") for i in a]
    #change to number for convenience
    for i in range(1,len(a)):
        a[i][1] = int(a[i][1],10)
    hd = a[0]
    #numpy.sort doesn't work as I intend here is alternative
    for i in range(1,len(a)-1):
        if(max_elem[0][1] < a[i][1]):
            max_elem[1][0] = max_elem[0][0]
            max_elem[1][1] = max_elem[0][1]
            max_elem[0][0] = a[i][0]
            max_elem[0][1] = a[i][1]
    for i in range(1,len(a)-1):
        if max_elem[1][1] < a[i][1] and max_elem[0][1] > a[i][1]:
            max_elem[2][0] = max_elem[1][0]
            max_elem[2][1] = max_elem[1][1]
            max_elem[1][0] = a[i][0]
            max_elem[1][1] = a[i][1]
    for i in range(1,len(a)-1):
        if max_elem[2][1] < a[i][1] and max_elem[1][1] > a[i][1]:
            max_elem[2][0] = a[i][0]
            max_elem[2][1] = a[i][1]
    total = a[len(a)-1]
    if header:
        return hd,(max_elem),(total)
    else:
        return (max_elem),(total)