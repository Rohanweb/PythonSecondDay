

class Employee():
    def __init__(self,name,ecode,salary):
        self._name=name
        self._ecode=ecode
        self._salary=salary

    def __repr__(self):
        return f"{self._name}, {self._ecode}, {self._salary}"

    @property
    def code(self):
        return self._ecode

    @code.setter
    def code(self,ecode):
        if ecode<0:
            self._ecode=101
        else:
            self._ecode=ecode


e=Employee("Prince",101,7878)

print(e.code)
e.code=-90
print(e.code)

