# 1
# 22
# 333
# 4444
n = int(input("nombres de lignes : "))
cnt = 0
for i in range(1,n+1):
    cnt += 1
    for j in range(i):
        print(cnt,end=" ")
    print("")
