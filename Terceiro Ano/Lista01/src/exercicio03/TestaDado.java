package exercicio03;

class TestaDado {
	public static void main(String[] args) {

		Dado d1, d2;

		d1 = new Dado();

		d2 = new Dado();

		d1.setNome("Dado da sorte");

		d2.setNome("Dado vermelho");

		// joga os dados

		d1.joga();

		d2.joga();

		int resultadoD1, resultadoD2;

		resultadoD1 = d1.mostra();

		resultadoD2 = d2.mostra();

		// mostra o valor de cada dado

		System.out.println("Valor do dado " + d1.getNome() + " eh: "

		+ resultadoD1);

		System.out.println("Valor do dado " + d2.getNome() + " eh: "

		+ resultadoD2);
	}
}
