## Simple # IDEA:
def first():
    second()
    print("First")

def second():
    third()
    print("Second")

def third():
    print("Final")

first()  ## Its kind of stored in a stack. LIFO, last method not stored. as stack methods
## called the methods are pop

def recurs(n):
    if n < 1:
        print("over")
    else:
        recurs(n-1)
        print('Recursion {}'.format(n-1))

recurs(4)

def poweroftwo(n):
    if n == 0:
        return 1
    else:
        return poweroftwo(n-1)*2

poweroftwo(3)

def factorial(n):
    assert n > 0 and isinstance(n,int)
    if n in (0,1):
        return 1
    else:
        return n*factorial(n-1)

factorial(10)
factorial(1.5) ## assertion error

def fib(n):
    assert n >= 0
    assert isinstance(n,int)
    if n in (0,1):
        return 1
    else:
        return fib(n-1) + fib(n-2)

fib(6)

def recursum(arr):
    if len(arr) == 1:
        return arr[0]
    else:
        return arr[len(arr)-1] + recursum(arr[:len(arr)-1])

recursum([1,2,3,10,20])

def recursumno(input):
    assert input >= 0
    if input < 10:
        return input
    else:
        return input%10 + recursumno(int(input/10))

recursumno(115)

def GCD(n,m):  ## not a good one
    maxn = max(n,m)
    minn = min(n,m)
    if maxn%minn == 0:
        return minn
    else:
        val = 2
        for val in range(2,minn+1):
            if n%val != 0 or m%val != 0:
                val += 1
            else:
                return val*GCD(int(n/val),int(m/val))
        return 1

GCD(60,72)
GCD(48,18)

def EucGCD(n,m):  ## no idea about this GCD algorithm
    maxn = max(n,m)
    minn = min(n,m)
    if minn == 0:
        return maxn
    else:
        return EucGCD(minn,maxn%minn)

EucGCD(48,18)

def sdectobinary(n):
    if n == 1:
        return str(1)
    else:
        return sdectobinary(int(n/2)) + str(n%2)

sdectobinary(4)

def reverse(string):
    if len(string) == 1:
        return string
    else:
        return reverse(string[1:]) + string[0]

reverse('rish')

def isPalindrome(string):
    output = reverse(string)
    if output.lower() == string.lower():
        return True
    else:
        return False

isPalindrome('rish')
isPalindrome('abccba')

def nestedevensum(object):
    sum = 0
    for key in object.keys():
        if isinstance(object[key],dict):
            sum = sum + nestedevensum(object[key])
        else:
            if isinstance(object[key],int):
                if object[key]%2 == 0:
                    sum += object[key]
                else:
                    pass
            else:
                pass
    return sum

obj = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 1,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

nestedevensum(obj)
