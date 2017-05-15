package exercicio02;

class Cronometro {
	private long inicio, fim;
	public void iniciar(){
		this.inicio = System.currentTimeMillis();
	}
	public void parar(){
		this.fim = System.currentTimeMillis();
	}
	public long mostrar(){
		return fim - inicio;
	}
}
