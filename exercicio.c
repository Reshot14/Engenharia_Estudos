/**Faça um programa em C que peça para digitar 3 números reais (variável tipo float), calcule e imprima a média dos números.
Responda a atividade com o programa e a tela de resultado.**/

#include <stdio.h>
#include <stdlib.h>
int main(){
//----
    printf("Digite o valor da nota1: ");

    float nota1; 
    scanf("%f" ,& nota1 );
//----
    printf("Digite o valor da nota2: ");

    float nota2;
    scanf("%f", & nota2);
//----
    printf("Digite o valor da nota3: ");

    float nota3;
    scanf("%f", & nota3);
//----
    printf("nota1 = %.2f\n",nota1);
    printf("nota2 = %.2f\n", nota2);
    printf("nota3 = %.2f\n", nota3);
//----
    float soma;
    soma = (nota1+nota2+nota3);
    printf("A soma dos termos é: %.2f\n", soma);
//----
    float media;
    media = (nota1+nota2+nota3)/3;
    printf("A media é: %.2f\n", media);

    return 0;
}
