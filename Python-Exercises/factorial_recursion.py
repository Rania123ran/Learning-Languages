num = int(input("saisir un nombre positif :"))
while (num<0):
    num = int(input("saisir un nombre positif ! :"))
def recursion(num):
    if(num ==0):
       return  1 
    else :
        return num * recursion(num - 1)
print("factorial est : ",recursion(num))
    