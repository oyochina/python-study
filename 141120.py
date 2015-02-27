import sys

sys.path.append('E:\my app\python')
from model1114 import becall



def search(*t,**d):
    keys=d.keys()
    values=d.values()
    print keys
    print values
    
search("one","two",oneA="1",twoA="2")
becall.test()
