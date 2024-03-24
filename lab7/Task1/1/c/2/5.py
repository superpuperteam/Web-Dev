n = int(input())
cnt = 0

while cnt < n:
    if 2**cnt > n:
        print(cnt)
        break

    cnt+=1