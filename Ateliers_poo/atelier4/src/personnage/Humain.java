package personnage;

public class Humain extends Personnage {
	
	private int nbDeplacements=0;
	private int niveau=1;

	public Humain(String nom, int age) {
		super(nom, age);
	}
	
	public void deplacer(int destination, int gain) {
		super.deplacer(destination,gain);
		nbDeplacements++;
		if (nbDeplacements==4) {
			niveau=2;
		}
		else if(nbDeplacements==6) {
			niveau=3;
		}
		
	}
	
	@Override
	public int positionSouhaite() {
		return getPosition()+(niveau*nbDeplacements);
	}
	
	public String toString() {
		return "Humain "+super.toString();
	}

}
