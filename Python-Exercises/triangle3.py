# *
# * *
# *   *
# *     *
# * * * * *
n = int(input("nombres de lignes : "))
for i in range (n+1):
    if(i == 0 or i == n) :
        for j in range(i):
            print("*",end=" ")
    else : 
        for k in range(i):
            if k == 0 or k == i-1 :
                print("*",end="")
            else : 
                print("  ",end="")
    print("")
