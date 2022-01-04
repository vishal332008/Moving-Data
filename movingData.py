
with open("file1.txt","r") as a:
    data_a = a.read()
    
with open("file2.txt","r") as b:
    data_b = b.read()

with open("file1.txt","w") as a:
    a.write(data_b)
    
with open("file2.txt","w") as b:
    b.write(data_a)
