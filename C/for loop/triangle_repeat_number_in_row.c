#include <stdio.h>
#include <stdlib.h>
/*
The pattern like :
 1
 22
 333
 4444
*/
int main(){
        int n , k = 1 ;
printf("entrer le nombre de ligne :");
scanf("%d",&n);
for(int i=1;i<=n;i++){
    for(int j= 1;j<=i;j++){
            printf("%d",k);

}
k++ ;
printf("\n");}}

