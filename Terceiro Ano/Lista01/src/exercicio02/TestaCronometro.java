package exercicio02;

class TestaCronometro {
	public static void main(String[] args) {

		long tempoGasto;

		Cronometro c = new Cronometro();

		// dispara cron�metro

		c.iniciar();

		// executa uma tarefa qualquer, como por exemplo, imprimir na tela de 0 a 1000

		for (int i = 0; i <= 1000; i++) {

		System.out.println(i);

		}

		// p�ra cron�metro ap�s o t�rmino da atividade

		c.parar();

		// pega o tempo que o cron�metro est� �mostrando�, conforme tempo gasto

		tempoGasto = c.mostrar();

		// mostra tempo gasto

		System.out.println("O tempo que java gastou foi: " + tempoGasto + "ms");
	}
}
