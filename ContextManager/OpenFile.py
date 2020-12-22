
class OpenFile:
    def __init__(self,destination,mode):
        self.destination=destination
        self.mode=mode

    def __enter__(self):
        print("Entering Context/Initializing Context")
        self.file=open(self.destination,self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("Exiting Context")
        return self.file.close()


with OpenFile("Testing","a+") as test:
    test.write("Demo Data \n")

print(test.closed)
print("Exiting Code")

