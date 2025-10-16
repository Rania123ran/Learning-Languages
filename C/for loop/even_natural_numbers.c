#include <stdio.h>
#include <stdlib.h>
/*
Test Data :
Input number of terms : 5
Expected Output :
The even numbers are :2 4 6 8 10
The Sum of even Natural Number upto 5 terms : 30
*/
int main(){
printf("Input number of terms : ");
int n ,s = 0 ;
scanf("%d",&n);
printf("The even numbers are :");
for(int i =1 ; i<=n ;i++){
    printf(" %d ",i*2);
    s += i*2;
}
printf("\nThe Sum of even Natural Number upto 5 terms :%d",s);
}
