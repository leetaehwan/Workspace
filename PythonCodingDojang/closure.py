def countdown(n):
    i = n + 1
    def cdown():
        nonlocal i
        i-=1
        return i
    return cdown

n = int(input())
 
c = countdown(n)
for i in range(n):
    print(c(), end=' ')