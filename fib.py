def fib(N):
    if N == 0:
        return 1
    elif N == 1:
        return 1
    a,b = 0,1
    for x in range(N):
        a ,b = b, a+b
    return b

fib(0)
fib(1)
fib(2)
fib(3)
fib(4)
fib(500)