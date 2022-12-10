a={"(":1,")":-1,"[":2,"]":-2,"{":3,"}":-3}
s=input("enter")
counter=0
for i in s:
    if i in a:
        counter+=a[i]
    else:
        pass
if counter==0:
    print("True")
else:
    print("False")