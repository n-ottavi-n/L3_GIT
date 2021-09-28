package formes_3d;


public class Sphere extends Forme3d {
	
	private double rayon;
	
	public Sphere(double rayon) {
		super();
		this.rayon=rayon;
	}
	
	public double getRayon() {
		return rayon;
	}

	@Override
	public double calcVolume() {
		// TODO Auto-generated method stub
		return (4*Math.PI*(Math.pow(rayon, 3)))/3;
	}

	@Override
	public double calcSurface() {
		// TODO Auto-generated method stub
		return 4*Math.PI*(Math.pow(rayon, 2));
	}
	
	public boolean equals(Object obj) {
		boolean res=false;
		if((obj!=null) && (obj instanceof Sphere)) {
			Sphere objSphere=(Sphere)obj;
			res=(objSphere.getRayon()==this.rayon);
		}
		return res;
	}

}
