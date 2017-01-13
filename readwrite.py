def read():
    f=open("input",'r')
    line=f.readline()
    split=line.split()
    a=split[2]
    print(a)
    for line in f:
        print(line)

    #clean up
    f.close()
