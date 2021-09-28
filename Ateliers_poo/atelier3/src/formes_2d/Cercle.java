package formes_2d;


public class Cercle extends Ellipse {
	
	
	public Cercle(float rayon) {
		super(rayon,rayon);
	}
	
	private double getRayon() {
		// TODO Auto-generated method stub
		return demiGrandAxe;
	}

	@Override
	public double calcPerimetre() {
		// TODO Auto-generated method stub
		return 2*Math.PI*demiGrandAxe;
	}

	
	public boolean equals(Object obj) {
		boolean res=false;
		if((obj !=null) && (obj instanceof Cercle)) {
			Cercle objCercle=(Cercle)obj;
			res=(objCercle.getRayon()==this.demiGrandAxe);
		}
		return res;
	}

	
	
	
	

}
