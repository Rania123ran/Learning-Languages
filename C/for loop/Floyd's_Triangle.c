#include <stdio.h>
#include <stdlib.h>
/*
1
01
101
0101
10101
*/
int main(){
   int n ,m = 1 ;  printf("entrer le nombre de ligne : "); scanf("%d",&n);
   for(int i = 1;i<=n ;i++){
    for(int j = 1 ; j<=i;j++){
        printf("%d",m);
        m-- ;
        if(m<0) m = 1 ;

    }
    printf("\n");

   }

}
