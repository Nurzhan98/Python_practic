def f(a):
    if a==0:
        return 1
    else:
        a = (a-1)*f(a)
f(5)