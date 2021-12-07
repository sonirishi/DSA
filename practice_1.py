import numpy as np

np.round(1.23,0)  ## round closest multiple to 10 (n=1 means 10^-1)
np.round(18.5,-1)
np.round(14.99,-1)
np.round(15,-1)
np.round(1.25,1)
np.round(1.35,1)  ## rounds to closest to 0 in cae of tie but the least signficant is even
np.around(15,-1)  ## leading rrailing 0s dont count
np.around(25,-1)
## this logic avoids the rounding errors to some extent e.e taking avg or sum (less biased)
import decimal
from decimal import Decimal
decimal.getcontext()  # default context
decimal.localcontext(ctx=None)

ctx = decimal.getcontext()
ctx.prec
ctx.rounding  ## default used for float, bankers rounding
x = Decimal('1.35')
with decimal.localcontext() as ctx:
    ctx.prec = 2
    ctx.rounding = decimal.ROUND_HALF_UP## operation withing this block uses local, outside will be global
    print(round(x,1))
print(Decimal(0.1))
# context precision impacts the maths not constructor
decimal.getcontext().prec = 2
x = Decimal('0.12345'); y = Decimal('0.12345')
x+y
print(x)

format(0.1,'.25f')
format(Decimal('0.1'),'.25f')

# if we use math module for decimal it will coerce to float first hence useless
decimal.getcontext().prec=28
a=Decimal('1.5')
a.ln()
from math import log
log(a)
## decimal is slower than float

import sys

a = Decimal('3.1415')
b = 3.1415

sys.getsizeof(a)
sys.getsizeof(b)

import time

def runfloat(n):
    for i in range(n):
        a = 3.1415

def rundec(n):
    for i in range(n):
        a = Decimal('3.1415')

n = 10000000
start = time.perf_counter()
runfloat(n)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
rundec(n)
end = time.perf_counter()
print(end-start)
 ## very slow compared to float

 def runfloat(n):
     a = 3.1415
     for i in range(n):
         a+a

 def rundec(n):
     for i in range(n):
         a = Decimal('3.1415')
         a+a

start = time.perf_counter()
runfloat(n)
end = time.perf_counter()
print(end-start)

start = time.perf_counter()
rundec(n)
end = time.perf_counter()
print(end-start)

issubclass(bool,int)
isinstance(True,bool)
isinstance(True,int)

id(True) == id(1)
## is checks the memory location
## precedence of and is higher than or. not is higher than and
## python has short circuiting in the booleans.

if stock in watch_list:
    if price > threshold:
        return True
# is same as
if stock in watch_list and price > threshold:
## if first evaluated to false and as its and condition second wont be evaluated
    return True

## null -> None

a = 10
b = 0
if b > 0 and a/b > 2:
    print('Stud')
# or ->  if x is true then return x else evaluate y and return it
1 or 1/0
0 or 1/0  # gives error

[1,2] is [1,2]  # not singleton

'key' in {'key':1}
1 in {'key':1}   ## looks for keys and not sort_values
