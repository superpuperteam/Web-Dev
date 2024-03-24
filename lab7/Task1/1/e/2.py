def power(a, n):
    cnt=1
    for i in range(n):
        cnt*=a
    
    return cnt

a = int(input())
n = int(input())

print(power(a,n))