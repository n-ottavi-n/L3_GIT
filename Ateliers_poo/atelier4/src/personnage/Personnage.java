package personnage;

import joueur.Joueur;

public abstract class Personnage {
	
	private String nom;
	private int age;
	private int position;
	public Joueur proprietaire;
	
	public Personnage(String nom, int age) {
		this.nom=nom;
		this.age=age;
		
	}
	
	public int getPosition() {
		return position;
	}
	
	public String getName() {
		return nom;
	}
	
	public void setProprietaire(Joueur p) {
		this.proprietaire=p;
	}
	
	public void deplacer(int destination, int gain) {
		position=destination;
		proprietaire.modifierPoints(Math.abs(gain));
	}
	
	public void penaliser(int penalite) {
		proprietaire.modifierPoints(-penalite);
	}
	
	public String toString() {
		return nom;
	}
	
	public abstract int positionSouhaite();
	


}
