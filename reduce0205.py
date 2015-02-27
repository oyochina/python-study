from functools import reduce
def fn(x,y):
    return x*10+y

X=[1,3,5,7,9]
Y=reduce(fn,X)


def fnadd(x,y):
    return x+y

X1=range(0,101)
Y1=reduce(fnadd,X1)
print(Y1)
