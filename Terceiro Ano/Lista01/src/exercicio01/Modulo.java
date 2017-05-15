package exercicio01;

class Modulo {
	private String titulo, descricao, professor;
	private double cargaHoraria;
	private double iniciado, concluido;
	public String getTitulo() {
		return titulo;
	}
	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}
	public String getDescricao() {
		return descricao;
	}
	public void setDescricao(String descricao) {
		this.descricao = descricao;
	}
	public String getProfessor() {
		return professor;
	}
	public void setProfessor(String professor) {
		this.professor = professor;
	}
	public double getCargaHoraria() {
		return cargaHoraria;
	}
	public void setCargaHoraria(double cargaHoraria) {
		this.cargaHoraria = cargaHoraria;
	}
	public double getIniciado() {
		return iniciado;
	}
	public void setIniciado(double iniciado) {
		this.iniciado = iniciado;
	}
	public double getConcluido() {
		return concluido;
	}
	public void setConcluido(double concluido) {
		this.concluido = concluido;
	}
}