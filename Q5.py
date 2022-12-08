# s="babad"
s="cbbd"
def palindrome(a):
    ans=True
    for i in range(len(a)//2 +1):
        if a[i] != a[len(a)-1-i] :
            ans=False
            break
    return ans
def a(a):
    ans=""
    for i in range(len(a)//2):
        for j in range(len(a),i,-1):
           if  True == palindrome(a[i:j+1]):
               ans=a[i:j+1] if len(a[i:j+1])>=len(ans) else ans

    return ans

print(a(s))

