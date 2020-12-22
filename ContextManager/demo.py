
f=open("sample.txt","a+")
f.write(' Some more data added \n')
f.close()

with open("sample.txt","a+") as f:
    f.write(" Another data added \n")

