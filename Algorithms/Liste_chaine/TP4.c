/*Exercice 1 (Cr�ation d�une liste):
#En vous inspirant des exemples du cours, �crire un programme qui construit une
#liste de 100 �l�ments contenant des nombres entiers choisis al�atoirement dans
#l�intervalle [0;100[.*/

#include <stdio.h>
#include <stdlib.h>
#include <time.h>
typedef struct Element{
int val ;
struct Element *suivant ;
}Liste ;
Liste *newElem (int val){
    Liste *newElem = (Liste*)malloc(sizeof(Liste));
    newElem -> val = val ;
    newElem -> suivant = NULL ;
    return newElem ;
    }
/*Exercice 2 (Recherche de valeur):
En utilisant le programme pr�c�dent pour la cr�ation de la liste, �crire une
fonction qui recherche une valeur donn�e dans une liste, et fournit un r�sultat
bool�en selon que la valeur recherch�e existe ou pas (0 ou 1). Quelle est la
complexit� de votre algorithme?*/
/*-----------------------------------------------*/
int chercher(Liste *tete ,int n){
    Liste *L = tete ;
    while(L != NULL){
        if(L->val == n){
            return 1 ;}
        else {L = L->suivant ;}
    }
    return 0;
}
//------------------------------------------------
/*Exercice 3 (Suppression d�un �l�ment):
En utilisant le programme de cr�ation de liste, �crire une fonction qui recherche
et supprime le n�ud comportant la valeur minimale de la liste.*/
//------------------------------------------------
void supp(){
int max;
if (tete != NULL) {
    max = tete->val;
    Liste *t = tete->suivant;
    while (t != NULL) {
        if (t->val > max) {
            max = t->val;
        }
        t = t->suivant;   }

}
int main(){
    srand(time(NULL));
    Liste *tete = NULL ;

    for(int i=0;i<100;i++){
        Liste* nvElem = newElem( rand() % 100);
        nvElem ->suivant = tete ;
        tete = nvElem ;
    }
    /*affichage*/
    int j = 1 ;
    Liste *t = tete;
    while(t != NULL ){

        printf("Element %d : %d \n",j,t->val);
        j++ ;
         Liste* elem = tete;
        t = t->suivant ;
    }
    int n ,m ;
    printf("veuillez saisir une valeur a chercher :");
    scanf("%d",&n);
    m = chercher(tete,n);
    if(m ==1){
        printf("la valeur existe dans la liste .\n");
    }
    else {
        printf("la valeur n'existe pas  dans la liste .\n");
    }


}



