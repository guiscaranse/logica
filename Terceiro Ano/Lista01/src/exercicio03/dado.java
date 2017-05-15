package exercicio03;

import java.util.Random;

class Dado {
	private int resultado;
	private String nome;
	public String getNome() {
		return nome;
	}
	public void setNome(String nome) {
		this.nome = nome;
	}
	public void joga(){
		Random r = new Random();
		this.resultado = 1 + r.nextInt(6);
	}
	public int mostra(){
		return resultado;
	}
}
