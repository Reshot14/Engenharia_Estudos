#include <stdio.h>

int main(){
    float valorProduto;
    float valorDesconto;
    float valorFinal;

    printf("\nDigite o valor do produto: ");
    scanf("%f",&valorProduto);

    printf("Digite o valor do desconto: ");
    scanf("%f",&valorDesconto);

    valorFinal = valorProduto - (valorProduto*(valorDesconto/100));

    printf("\nO valor final coom desconto: %0.2f\n\n", valorFinal);

}