st=str(input("Enter the string: "))
numcount=0
upcount=0
lowcount=0
spcount=0
for i in range(0,len(st)):
    if st[i].isdigit():
        numcount+=1
    if st[i].isupper():
        upcount+=1
    if st[i].islower():
        lowcount+=1
    else:
        spcount+=1
print("Uppercase characters:",upcount)
print("Lowercase characters:",lowcount)
print("Numeric characters:",numcount)
print("Special characters:",spcount)
