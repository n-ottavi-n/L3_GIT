package formes;

public abstract class Forme {
	
	private static int numForme=0;
	public final String ID_FORME;
	
	public Forme() {
		numForme++;
		ID_FORME="_"+numForme;
	}
	
	public abstract double calcSurface();
	
	public boolean estLaPlusGrande(Forme forme) {
		return this.calcSurface()>forme.calcSurface();
	}
	
	public String toString() {
		return ID_FORME+" de surface: "+calcSurface();
	}

}
