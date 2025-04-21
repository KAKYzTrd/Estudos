import java.util.Scanner;

public class Main {
	public static void main(String[] args) {
	  Scanner input = new Scanner(System.in);
	  
	  System.out.print("\033[H\033[2J");
	  System.out.flush();
	  
	  System.out.print("Qual é melhor? Java (J) ou Python (p)\n > ");
	  String resposta = input.nextLine().trim().toUpperCase();
	  
	  if (resposta.equals("J")) {
	    System.out.println("\n Java é a linguagem GOAT");

	  } else if (resposta.equals("P")) {
	    System.out.println("\n Sai pra la coda fofo Python e coisa de viado");

	  };
	}
}
