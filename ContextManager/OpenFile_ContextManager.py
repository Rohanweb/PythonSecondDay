from contextlib import contextmanager

@contextmanager
def open_file(file,mode):
    try:
        f=open(file,mode)
        yield f
        print("About to Exit the Context Manager")
    finally:
        f.close()

with open_file("Testing1","a+") as f:
    f.write("Another Testing Demo \n")
    print("some data printed")
    for _ in range(10):
        print("Hello")

print(f.closed)