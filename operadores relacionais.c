#include <stdio.h>
int main(){
    //declarando variaveis
    int idade;
    //solicitacao da idade (entrada)
    printf("\nDigite sua idade: ");
    scanf("%d",&idade);

    //verficacao da idade ( processamento e saida)
    if(idade>=18){
        printf("Maior de idade");
    }else{
        printf("Menor de idade");
    }

    if((idade%2)==0){
        printf("\nPar\n");
    }else{
        printf("\nímpar\n");
    }
    return 0;
}