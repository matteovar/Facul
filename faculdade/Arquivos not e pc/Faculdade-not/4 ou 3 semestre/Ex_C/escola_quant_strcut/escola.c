#include <stdio.h>

struct escola {
    char nome[25];
    int matricula;
    float notas[2];
    float media;
};

int main() {
    
    int qnt_alunos;

    printf("Digite a quantidade de alunos: ");
    scanf("%d",&qnt_alunos);

    struct escola aluno[qnt_alunos];
    for (int i = 0; i < qnt_alunos;i++){
        printf("Digite o nome do aluno: ");
        scanf("%s", aluno[i].nome);

        printf("Digite a matricula do aluno: ");
        scanf("%d", &aluno[i].matricula);

        printf("Digite a nota 1 do aluno: ");
        scanf("%f", &aluno[i].notas[0]);

        printf("Digite a nota 2 do aluno: ");
        scanf("%f", &aluno[i].notas[1]);

        aluno[i].media = (aluno[i].notas[0] + aluno[i].notas[1]) / 2;
        printf("-----------Dados dos alunos ----------\n");
        printf("Nome: %s\n", aluno[i].nome);
        printf("Matricula: %d\n", aluno[i].matricula);
        printf("Media: %.2f\n", aluno[i].media);
        printf("\n");
    }

    return 0;
}