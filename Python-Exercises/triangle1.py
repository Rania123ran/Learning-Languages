# 1
# 12
# 123
# 1234
# 12345
n = int(input("nombres de lignes : "))
for i in range(n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")