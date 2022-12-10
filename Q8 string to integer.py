import sys
s="-91283472332"
s=s.strip(" ")
def fi(s):
    k=""
    if s[0].isalpha() :
        k="0"
    elif int(s)< -sys.maxsize-1:
        k=f"{sys.minsize}"
    else :
        for i in s:
            if i.isnumeric() or i=="-" :
                k=k+i
            else :
                pass
    return k
print(fi(s))