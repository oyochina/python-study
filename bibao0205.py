def count():
    fs = []
    for i in range(1, 4):
        def f(h):
            #def g():
            #    return j*j
            return lambda :h*h
            #return g
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1(),f2(),f3())




#def count():
#    fs = []
#    for i in range(1, 4):
 #       def f(i):
 #            return i*i
#        fs.append(f)
#    return fs

#f1, f2, f3 = count()
#print(f1(),f2(),f3())
