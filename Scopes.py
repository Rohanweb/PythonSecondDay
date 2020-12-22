'''
LEGB
Local, Enclosing, Global, Built-in
'''




for a in range(2):
    x = 'global {}'.format(a)


def outer():
    # x = 'outer x'
    for b in range(3):
        x = 'outer {}'.format(b)

    def inner():
        # x = 'inner x'
        for c in range(4):
            x = 'inner {}'.format(c)
        print(x)
        print(a, b, c)

    inner()
    print(x)
    print(a, b)

outer()
# print(x)
# print(a)



x=10
y=20

def abc():
    z=90
    x=800
    a=10
    print(locals())

class xyz():
    test="Something"

    @classmethod
    def changeTest(cls,vals):
        cls.test=vals

    def __init__(self,p,q):
        self.ppp=p
        self.qqq=q
    def localmethod(self):
        print(vars(self))


print (globals())
abc()
print (globals())

obj=xyz(90,80)
obj1=xyz(660,840)
print(obj.ppp)
print(obj1.ppp)
print(obj.test)
print(obj1.test)
obj.changeTest("Anything")
print(obj.test)
print(obj1.test)


obj.localmethod()