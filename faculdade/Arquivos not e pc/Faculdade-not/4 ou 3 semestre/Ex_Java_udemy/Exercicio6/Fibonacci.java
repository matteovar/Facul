//Matteo Domiciano Varnier - 32158238
package Exercicio6;

import java.util.Scanner;

public class Fibonacci {
    public static void main(String[] args){
        Scanner s = new Scanner(System.in);

        System.out.print("Digite o tamanho da sequencia: ");
        int n = s.nextInt();

        int a = 1;
        int b = 1;
        int c;

        for(int i=0;i<n;i++){
            System.out.print(a+" ");
            c=a+b;
            a=b;
            b=c;
        }

        

        s.close();
    }
}
