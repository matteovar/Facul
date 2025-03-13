//Matteo Domiciano Varnier - 32158238
package Exercicio2;

import java.util.Scanner;

public class VogalouNao {
    public static void main(String[] args) {
        Scanner s = new Scanner(System.in);
        char letra ;

        System.out.printf("Digite uma letra para saber se é vogal ou nao: ");
        letra = s.next().toLowerCase().charAt(0);

        if (letra == 'a' || letra == 'e' || letra == 'i' || letra == 'o' || letra == 'u'){
            System.out.println("A letra é vogal");
        }else{
            System.out.println("A letra é consoante");
        }
        s.close();
    }
    
}
