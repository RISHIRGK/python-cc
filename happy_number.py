def happy(n):
    if n == 1:
        return True
    if n == 4:
        return False
    ans = 0
    for i in str(n):
        ans += int(i) ** 2

    return happy(ans)


for i in range(1,100):
    print(i,happy(i))
# print(happy(11))
# print(happy(10))
