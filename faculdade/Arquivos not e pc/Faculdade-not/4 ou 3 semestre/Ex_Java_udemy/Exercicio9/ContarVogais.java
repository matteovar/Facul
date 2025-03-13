//Matteo Domiciano Varnier - 32158238
package Exercicio9;

public class ContarVogais {
    public static int contarVogais(String s) {
        int cont = 0;
        for (int i=0 ; i<s.length(); i++){
            char letra = s.charAt(i);
            if(letra == 'a'|| letra == 'e'|| letra == 'i' ||letra == 'o' ||letra == 'u'||letra == ' '){
               cont ++;
            }
        }
        return cont;
    }   
}
