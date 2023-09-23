#include <stdio.h>
int main(){
    //declaracao das variaveis
    char sinal;
    float oper1, oper2, resultado=0;

    //obtencao dos valores(entrada)

    printf("Operadores: ");
    printf("\n - * / ");
    printf("\nDigite o caractere da operação: ");
    scanf("%c", &sinal);
    fflush(stdin);//limpar o buffer do teclado

    while(sinal!= '+' && sinal!='-' && sinal!='*' && sinal!='/' ){
        //validacao para o caractere invalido
        printf("\nOperador invalido, Digite novamente: ");
        printf("\n - * / ");
        scanf("%c", &sinal);
        fflush(stdin);//limpar o buffer do teclado
    }
    printf("Digite o operando 1: ");
    scanf("%f", &oper1);
    printf("Digite o operando 2: ");
    scanf("%f", &oper2);

    while(sinal=="/" && oper2==0)//divisao por 0 nao pode)
    {
        printf("\nDivisao por zero é invalida");
        printf("\nDigite o operando 2: ");
        scanf("%f", &oper2);
    }

    //calculo da operacao(processamento)

    switch(sinal){
    case '+':
        resultado = oper1 + oper2;
        break;

    case '-':
        resultado = oper1 - oper2;
        break;

    case '*':
        resultado = oper1 * oper2;
        break;

    case '/':
        resultado = oper1 / oper2;
        break;
        
    }

    //exibicao do resultado(saída)
    printf("\n%0.1f %c %0.1f = %0.1f\n", oper1,sinal,oper2,resultado);

    return 0;}