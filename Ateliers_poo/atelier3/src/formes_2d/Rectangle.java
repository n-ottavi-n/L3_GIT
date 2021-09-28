package formes_2d;

public class Rectangle extends Forme2d {
	
	private double longueur;
	private double largeur;
	
	public Rectangle(double a,double b) {
		super();
		longueur=a;
		largeur=b;
	}

	public double getLongueur() {
		return longueur;
	}
	
	public double getLargeur() {
		return largeur;
	}
	
	@Override
	public double calcPerimetre() {
		// TODO Auto-generated method stub
		return 2*(longueur+largeur);
	}

	@Override
	public double calcSurface() {
		// TODO Auto-generated method stub
		return longueur*largeur;
	}
	
	public boolean equals(Object obj) {
		boolean res=false;
		if((obj!=null) && (obj instanceof Rectangle)) {
			Rectangle objRectangle=(Rectangle)obj;
			res=(objRectangle.getLongueur()==this.longueur&&
					objRectangle.getLargeur()==this.largeur);
		}
		return res;
	}

}
