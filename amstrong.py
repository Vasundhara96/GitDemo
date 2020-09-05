n=int(input("ENTER THE NUMBER: "))
no=n
res=0
length=len(str(n))
i=0
while i < length:
    num=n%10
    res=res+num**3
    n=n//10
    i+=1
if no==res:
    print ("AMSTRONG")
else:
    print ("NOT AN AMSTRONG")
    
