## arguments are passed as reference hence memory address is passed
def my_func(a,b,c):
    print("a={0:.3f},b={1},c={2}".format(a,b,c))
my_func(1,2,3)
1,2,3   ## comma indicates a tuple not brackets
(1) ## its an int
# python evaluate right hand side first and assign to lhs
#dictionary and sets are unordered types
d = {'a':1,'b':2,'c':3}
sorted(d,key=d.get,reverse=True)
d.items()
a,*b = [1,2,3,4,5]
print(a,b)
a,*b,c=[1,2,3,4,5]
print(a,b,c)
# * operator works for any iterable
d1 = {'a':1,'b':2,'c':3}
d2 = {'d':1,'e':2,'f':3}
d3 = {'f':1,'g':2,'h':3}

{**d1}

{**d1,**d2,**d3}
# set object doesnt support indexing
a,b,*c,d = 'rishabh'
print(a,b,c,d)
st = 'rishabh'
a,b,c,d = st[0],st[1],st[2:-1],st[-1]
print(a,b,c,d)
*c, = c
print(c)
list(c)
l = [1,2,3,'rishabh']
a,*b,(c,d,*e) = l
print(a,b,c,d,e)
a,b,c,d,e = l[0],l[1:-1],l[-1][0],l[-1][1],l[-1][2:-1]
print(a,b,c,d,e)

def my_func(a,b,*args):  ## *args end with tuple, in unpacking we were getting list
    print(a,b,*args)
    print(a,b,args)

my_func(1,2,3,4)
a,b,c=[1,2,3]
print(a)
## default value is created for function when fun is defined and not when func is run
## hence if we default it to sys datetime, if the func is loaded the sys datetime will remain same
## if we have mutable object for default then it can change
def my_func(a,b,**kwargs):  ## *args end with tuple, in unpacking we were getting list
    print(a,b,kwargs)
    print(kwargs['e'])

my_func(1,2,e=10,f=5)

l = ['v','B','a','Y']
sorted(l)

sorted(l,key=lambda z: z.upper())
ord('a')
from random import random
l = [1,2,3,4,5,6,7,8,9]
sorted(l,key=lambda x: x*random())

import inspect
from scipy.stats import norm
inspect.signature(norm)

def myfunc(a:'int',b:'int') -> 'None':
    return None

myfunc.__annotations__
myfunc.__doc__

def myfunc(a,b) -> str:
    return 'Pass'
callable(myfunc)

map(lambda x: x**2, [1,2,3])  ## returns iterator
list(map(lambda x: x**2, [1,2,3]))   # list converts iterator to list

list(map(lambda x: sum(x), list(zip([1,2,3],[3,4,5]))))
list(zip([1,2,3],[3,4,5]))
list(map(lambda x, y: x*y, [1,2,3],[1,2,3]))

list(filter(lambda x: x > 3, [2,3,4]))   # iterator returns Truthy returned
# pair wise combined
list(zip([1,2,3],[4,5,6],[6,7,8]))

rsults = (i**2 for i in range(10))
rsults
list(rsults)
## once generator is exhausted then  we cant resue it

from functools import reduce
reduce(lambda a,b: a if a>b else b, [3,1,6,3,8,10,4])
## iteratively apply function on some values with any iterable it works
## min max sum any all are reduce functions

from functools import partial
func = lambda x, y: x+y
f = partial(func,10)
f(20)
a=10
f = partial(func,a)
f(20)
a=100
f(20)  ## partial has baked in the earlier memory address of a now a points to something diff
## but partial points to same memory address
import operator as op
op.contains('rishabh','ris')
op.getitem([1,2,3,4], 1)
f = op.itemgetter(2)   ## think of it as partial function. it is callable
f([1,2,3,4])

a = 1000
def func():
    a = 10
    print(a)
## compile time a is local, masking global a

def func():
    global a
    a = 100
    print(a)

func()
a
## python uses intermediate cell which has memotry address of the value in case\
## of multi scoped variables

sorted([3,1,5,2,3,6])
sorted([3,1,5,2,3,6])[-2:]
import sys
sys.path.append('D:/Projects/venv1/Lib/site-packages/')
import pandas as pd
dict1 = {"wt":3,"round":100,"stop":5}
val = pd.DataFrame()
val.append(dict1,ignore_index=True)  ## cant take keyword argument

def counter():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = counter()
fn()
fn()  ### it increase by 1 from 1 initial value, closure is inc and count
f2 = counter()
f2()  ## f2 and fn have different closures
## closures are created at the start. free varuavkes are evaluated when we call the function

def adder(n):
    def inc(x):
        return x+n
    return inc

add_1 = adder(1)
add_1(3)
add_2 = adder(2)
add_2(3)
## Closures
fn.__code__.co_freevars
fn.__closure__

def counter(fn):
    cnt = 0
    def inner(*args,**kwargs):
        nonlocal cnt
        cnt += 1
        print("Function called {0} times".format(cnt))
        return fn(*args,**kwargs)
    return inner

def add(a,b):
    return a+b
def mult(a,b):
    return a*b

add_closure = counter(add)
add_closure(1,2)
add_closure(1,4)
mult_closure = counter(mult)
mult_closure(1,2)
add_closure.__closure__
add_closure.__code__.co_freevars

## decorator
# takes a function and returns closure
## closure accepts any args and kwargs

def deco(f):
    return lambda x: f(x + 1)

@deco
def myfunc(x):
    return 1 / x
 
if False:
    print('False')
else:
    print('True')

@counter
def add(a,b):
    return a+b

add.__closure__

import xgboost