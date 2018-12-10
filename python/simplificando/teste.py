import operator
def calcula(oper):
    a = 1
    b = 2
    c = oper(a,b)
    print(c)

calcula(operator.add)