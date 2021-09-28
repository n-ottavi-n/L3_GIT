package formes_2d;


public abstract class Forme2d extends formes.Forme {
	
	
	public Forme2d() {
		super();
	}
	
	public abstract double calcPerimetre();
	
	public String toString() {
		return "Forme 2D "+super.toString()+" et de perimetre: "+calcPerimetre();
	}
	
	
	

}
