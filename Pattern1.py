n=int(input("Enter the range: "))
m=n
for i in range(0,m):
    n=m-i
    for j in range(n,0,-1):
        print (j,end="")
    print ("\n")


