package formes_3d;

public class Cylindre extends Forme3d {
	
	private double rayon;
	private double hauteur;
	
	public Cylindre(double r, double h) {
		super();
		rayon=r;
		hauteur=h;
	}
	
	public double getRayon() {
		return rayon;
	}
	
	private double getHauteur() {
		return hauteur;
	}

	@Override
	public double calcVolume() {
		// TODO Auto-generated method stub
		return hauteur*(Math.PI*(Math.pow(rayon, 2)));
	}

	@Override
	public double calcSurface() {
		// TODO Auto-generated method stub
		return 2*Math.PI*rayon*(hauteur)+2*(Math.PI*Math.pow(rayon, 2));
	}
	
	public boolean equals(Object obj) {
		boolean res=false;
		if((obj!=null) && (obj instanceof Cylindre)) {
			Cylindre objCylindre=(Cylindre)obj;
			res=(objCylindre.getRayon()==this.rayon &&
					objCylindre.getHauteur()==this.hauteur);
		}
		return res;
	}


	
	

}
