//Matteo Domiciano Varnier - 32158238
package Exercicio3;

import java.util.Scanner;

public class Exercicio3 {
    public static void main(String[] args) {

        Scanner s = new Scanner(System.in);

        int maior = 0;
        int menor =  0;
        int n;

        for (int i = 0; i<10; i++){
            System.out.println("Digite o "+(i+1)+"º valor:");
            
            n = s.nextInt();

            if (i==0){
                maior = n;
                menor = n;
            }
            if (n > maior){
                maior= n;
            }
            if (n<menor){
                menor = n;
            }

        }

        System.out.println("O maior numero foi: "+maior+" e o menor numero foi: "+menor);
        s.close();
    }

}
