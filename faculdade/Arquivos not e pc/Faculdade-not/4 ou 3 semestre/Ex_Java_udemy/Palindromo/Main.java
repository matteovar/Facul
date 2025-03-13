//Felipe Mazzeo Barbosa - 32257023
//Matteo Domiciano Varnier - 32158238


import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner scanner = new Scanner(System.in);

    System.out.println("Digite um texto: ");
    String texto = scanner.nextLine();

    Palindromo palindromo = new Palindromo();
    palindromo.setTexto(texto);

    // verifica se o texto é um palíndromo ou não e exibe o resultado
    if (palindromo.verificaPalindromo()) {
      System.out.println("É um palíndromo!");
    } else {
      System.out.println("Não é um palíndromo.");
    }
    scanner.close();
  }
}

// Referencias:

// https://www.youtube.com/watch?v=kd3dr39rgrk
// https://www.youtube.com/watch?v=lhf8gaUx4yU
// https://javawithumer.com/2018/09/getters-and-setters-lesson-28.html7
// https://www.w3schools.com/java/java_encapsulation.asp
// https://docs.oracle.com/javase/tutorial/java/data/manipstrings.html
// https://www.educative.io/answers/how-to-check-if-a-string-is-a-palindrome-in-java