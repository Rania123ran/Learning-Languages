/*
Write a program in C to find the sum of the series [ 1-X^2/2!+X^4/4!- .........].
Test Data :
Input the Value of x :2
Input the number of terms : 5
Expected Output :
the sum = -0.415873
Number of terms = 5
value of x = 2.000000
*/
#include <stdio.h>
#include <stdlib.h>
int main(){
int x ; printf("Input the Value of x :") ; scanf("%d",&x);
int n ; printf("Input the number of terms : :") ; scanf("%d",&n);
float s = 0.0 ;
for(int i = 0;i<n;i++){
    int fac = 1 ;
    for(int j =1;j<=2*i;j++){
        fac *= j ;}
    s +=  pow(-1,i)*(pow(x,2*i)/fac) ;
}
printf("the sum  = %f",s);

}
