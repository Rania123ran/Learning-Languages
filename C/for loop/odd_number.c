#include <stdio.h>
#include <stdlib.h>
/*Input number of terms : 10
Expected Output :
The odd numbers are :1 3 5 7 9 11 13 15 17 19
The Sum of odd Natural Number upto 10 terms : 100*/
int main(){
    int n ,s = 0;
    printf("Input number of terms :");
    scanf("%d",&n);
    printf("The odd numbers are :");
    for(int i=1;i<=n;i++){
        printf("%d ",i*2-1);
        s += i*2-1 ;
    }
    printf("The Sum of odd Natural Number upto 10 terms : %d",s);

}
