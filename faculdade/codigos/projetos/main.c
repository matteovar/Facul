#include <stdio.h> // Inclusão da biblioteca padrão de entrada e saída em C
#include <stdlib.h> // Inclusão da biblioteca padrão de funções utilitárias em C
#include <string.h> // Inclusão da biblioteca para manipulação de strings em C

#define MAX_PALAVRAS 10000 // Definição do máximo de palavras no vetor
#define MAX_COMPRIMENTO 100 // Definição do tamanho máximo de cada palavra

// Função para ler palavras do arquivo de entrada
int lerPalavras(char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO], char* nome_arquivo) {
    FILE *arquivo = fopen(nome_arquivo, "r"); // Abrir o arquivo no modo leitura
    if (arquivo == NULL) { // Verificar se houve erro na abertura do arquivo
        printf("Erro ao abrir o arquivo.\n"); // Imprimir mensagem de erro
        exit(1); // Encerrar o programa
    }
    int contador = 0; // Inicializar contador de palavras lidas
    while (fscanf(arquivo, "%s", palavras[contador]) != EOF) { // Ler palavras do arquivo enquanto não chegar ao fim do arquivo (EOF)
        contador++; // Incrementar contador de palavras lidas
    }
    fclose(arquivo); // Fechar o arquivo
    return contador; // Retornar o número total de palavras lidas
}

// Função para escrever palavras ordenadas em um arquivo de saída
void escreverPalavras(char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO], int contador, char* nome_arquivo) {
    FILE *arquivo = fopen(nome_arquivo, "w"); // Abrir o arquivo no modo escrita
    if (arquivo == NULL) { // Verificar se houve erro na abertura do arquivo
        printf("Erro ao abrir o arquivo.\n"); // Imprimir mensagem de erro
        exit(1); // Encerrar o programa
    }
    for (int i = 0; i < contador; i++) { // Escrever cada palavra no arquivo de saída
        fprintf(arquivo, "%s ", palavras[i]);
    }
    fclose(arquivo); // Fechar o arquivo
}

// Função de ordenação Insertion Sort
void ordenarInsertionSort(char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO], int n, int* passos) {
    for (int i = 1; i < n; i++) { // Loop para percorrer o vetor de palavras
        char chave[MAX_COMPRIMENTO]; // Definir variável para armazenar a palavra chave
        strcpy(chave, palavras[i]); // Copiar a palavra atual para a chave
        int j = i - 1; // Definir o índice j como o anterior ao índice i
        while (j >= 0 && strcmp(palavras[j], chave) > 0) { // Loop para encontrar a posição correta da palavra chave
            strcpy(palavras[j + 1], palavras[j]); // Deslocar a palavra atual para a direita
            j = j - 1; // Decrementar j
            (*passos)++; // Incrementar o número de passos
        }
        strcpy(palavras[j + 1], chave); // Inserir a palavra chave na posição correta
    }
}

// Função de merge de dois subvetores
void merge(char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO], int esquerda, int meio, int direita, int* passos) {
    int i, j, k; // Definir variáveis de iteração
    int n1 = meio - esquerda + 1; // Calcular o tamanho do primeiro subvetor
    int n2 = direita - meio; // Calcular o tamanho do segundo subvetor

    char L[n1][MAX_COMPRIMENTO], R[n2][MAX_COMPRIMENTO]; // Definir vetores temporários para armazenar os subvetores

    for (i = 0; i < n1; i++) // Copiar o primeiro subvetor para L
        strcpy(L[i], palavras[esquerda + i]);
    for (j = 0; j < n2; j++) // Copiar o segundo subvetor para R
        strcpy(R[j], palavras[meio + 1 + j]);

    i = 0; // Inicializar o índice do primeiro subvetor
    j = 0; // Inicializar o índice do segundo subvetor
    k = esquerda; // Inicializar o índice do subvetor resultante
    while (i < n1 && j < n2) { // Loop para combinar os subvetores em ordem
        if (strcmp(L[i], R[j]) <= 0) { // Comparar as palavras do subvetor esquerdo e direito
            strcpy(palavras[k], L[i]); // Copiar a palavra do subvetor esquerdo
            i++; // Incrementar o índice do subvetor esquerdo
        } else {
            strcpy(palavras[k], R[j]); // Copiar a palavra do subvetor direito
            j++; // Incrementar o índice do subvetor direito
        }
        k++; // Incrementar o índice do subvetor resultante
        (*passos)++; // Incrementar o número de passos
    }

    while (i < n1) { // Copiar os elementos restantes do subvetor esquerdo
        strcpy(palavras[k], L[i]);
        i++;
        k++;
        (*passos)++;
    }

    while (j < n2) { // Copiar os elementos restantes do subvetor direito
        strcpy(palavras[k], R[j]);
        j++;
        k++;
        (*passos)++;
    }
}

// Função de ordenação Merge Sort
void ordenarMergeSort(char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO], int esquerda, int direita, int* passos) {
    if (esquerda < direita) { // Verificar se há mais de um elemento no subvetor
        int meio = esquerda + (direita - esquerda) / 2; // Calcular o ponto médio do subvetor
        ordenarMergeSort(palavras, esquerda, meio, passos); // Ordenar a metade esquerda do subvetor
        ordenarMergeSort(palavras, meio + 1, direita, passos); // Ordenar a metade direita do subvetor
        merge(palavras, esquerda, meio, direita, passos); // Combinar as metades ordenadas


          }
      }

      int main() {
          char palavras[MAX_PALAVRAS][MAX_COMPRIMENTO];
          int numPalavras;

          numPalavras = lerPalavras(palavras, "10.000_palavras.txt"); // Ler as palavras do arquivo de entrada

          int passos_insertion = 0;
          ordenarInsertionSort(palavras, numPalavras, &passos_insertion); // Ordenar usando Insertion Sort
          escreverPalavras(palavras, numPalavras, "out1.txt"); // Escrever as palavras ordenadas em um arquivo de saída

          int passos_merge = 0;
          ordenarMergeSort(palavras, 0, numPalavras - 1, &passos_merge); // Ordenar usando Merge Sort
          escreverPalavras(palavras, numPalavras, "out2.txt"); // Escrever as palavras ordenadas em um arquivo de saída

          printf("Passos do Insertion Sort: %d\n", passos_insertion); // Imprimir o número de passos do Insertion Sort
          printf("Passos do Merge Sort: %d\n", passos_merge); // Imprimir o número de passos do Merge Sort

          return 0;
      }