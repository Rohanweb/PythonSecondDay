
import requests
import inspect
import time
r=requests.get("https://yahoo.com")
#time.sleep(5)
print(inspect.isclass(r))
#print(inspect.getsource(requests.Response))
print(inspect.getdoc(requests.Response))

class Demo():
    pass

class MyDemo(Demo):
    pass

class NewDemo(MyDemo):
    pass

t=inspect.getclasstree([NewDemo])
param=inspect.signature(requests.get)

for i in param.parameters.values():
    print(i.kind)

print(param)

