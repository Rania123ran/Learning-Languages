# 1634 = 1^4 + 6^4 + 3^4 + 4^4  = 1 +1296 + 81 +256 (n = 4)
number1 = int(input("Saisir un nombre : "))
number2 = number1
sum  = 0
def tailleNumber(A):
    B = 0
    while A != 0:
        A//=10 
        B+=1
    return B
puis = tailleNumber(number1)
while number1 != 0 :
    rest = number1 % 10 
    sum += rest**puis
    number1 //= 10
if(sum == number2):
    print(number2," is an Armstrong number")
else :
    print(number2," is not an Armstrong number")
    
       
    
     






