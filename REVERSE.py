n=int(input("Enter the number: "))
length=len(str(n))
i=0
res=[]
while i<length:
    num=n%10
    res.append(num)
    n=n//10
    i+=1
for i in res:
    print (i,end="")
