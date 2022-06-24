nn = '#'
#######################################################
print(f'{nn:#^60}')
n = ' Lambda '
print(f'{n:#^60}')
#######################################################
def f1(arg, arg2):
    return arg * arg2
# iguais
f2 = lambda arg, arg2: arg * arg2

var1 = f1(2,4)
var2 = f2(2,4)
print(var1)
print(var2)
#######################################################
print(f'{nn:#^60}')
#######################################################
l = [
    ['p1', 20],
    ['p2', 10],
    ['p3', 30],
    ['p4', 25],
    ['p5', 5]
]
def f(x):
    print(x[1])
    return x[1]
print(l)
l.sort(key=f)
print(l)
l.sort(key=f, reverse=True)
print(l)
#######################################################
print(f'{nn:#^60}')
#######################################################
l2 = [
    ['p1', 20],
    ['p2', 10],
    ['p3', 30],
    ['p4', 25],
    ['p5', 5]
]
print(l2)
l2.sort(key=lambda y: y[1])
print(l2)
l2.sort(key=lambda x: x[1], reverse=True)
print(l2)
#######################################################
print(f'{nn:#^60}')
#######################################################
l3 = [
    ['p1', 20],
    ['p2', 10],
    ['p3', 30],
    ['p4', 25],
    ['p5', 5]
]
def f3(x):
    return x[1]
print(l3[1])
print(1)
print(sorted(l3, key=lambda i: i[1], reverse=True))
print(2)
print(l3)


