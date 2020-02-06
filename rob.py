import pro
g=pro.g*10
def fib2(n):   # return Fibonacci series up to n
    result=[]
    a, b = 0, 1
    while a < n:
        result.append(a)
        a, b = b, a+b
        print(result)
    return result
    return b


def add(a, b):
    # returning sum of a and b
    return a + b



