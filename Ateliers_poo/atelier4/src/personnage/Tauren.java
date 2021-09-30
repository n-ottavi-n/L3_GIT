package personnage;



public class Tauren extends Personnage {
	
	private int taille;
	
	public Tauren(String nom, int age, int taille) {
		super(nom, age);
		this.taille=taille;
	}

	@Override
	public int positionSouhaite() {
		return (getPosition())+(int)((Math.random()*taille-1)+1);
	}
	
	public String toString() {
		return "Tauren "+super.toString();
	}

	
	

}
