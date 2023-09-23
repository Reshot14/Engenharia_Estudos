#include  <stdio.h>

int main() {
    // criacao das variaveis
    char nome[50];
    int idade;
    char sexo;
    char profissao[50];
    float salario;

    //soicitacao dos valores
    printf("\nDigite os seus dados.\n");

    //solicitacao do nome
    printf("Nome: ");
    scanf("%s", nome);
    fflush(stdin); // especificidade da linguagem c. limpar o buffer de entrada 

    //solicitacao do idade
    printf("Idade: ");
    scanf("%d",&idade );
    fflush(stdin);

    //solicitacao do sexo
    printf("sexo: ");
    scanf("%c", &sexo);
    fflush(stdin);

    //solicitacao do profissao
    printf("Profissao: ");
    scanf("%s", profissao);
    fflush(stdin);


    //solicitacao do salario
    printf("Salario: ");
    scanf("%f", &salario);
    fflush(stdin);

    //exibicao na tela
    printf("\nOla, %s. Segue a baixo os seus daods.", nome);
    printf("\n Idade: %d anos", idade);
    printf("\n sexo: %c", sexo);
    printf("\n profissao: %s", profissao);
    printf("\nSalario: %.2f", salario);

    return 0;


} 