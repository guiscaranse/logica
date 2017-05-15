package exercicio02;

class TestaCronometro {
	public static void main(String[] args) {

		long tempoGasto;

		Cronometro c = new Cronometro();

		// dispara cronômetro

		c.iniciar();

		// executa uma tarefa qualquer, como por exemplo, imprimir na tela de 0 a 1000

		for (int i = 0; i <= 1000; i++) {

		System.out.println(i);

		}

		// pára cronômetro após o término da atividade

		c.parar();

		// pega o tempo que o cronômetro está “mostrando”, conforme tempo gasto

		tempoGasto = c.mostrar();

		// mostra tempo gasto

		System.out.println("O tempo que java gastou foi: " + tempoGasto + "ms");
	}
}
