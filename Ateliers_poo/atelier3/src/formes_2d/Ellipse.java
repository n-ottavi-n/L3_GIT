package formes_2d;

public class Ellipse extends Forme2d {
	
	protected double demiGrandAxe;
	protected double demiPetitAxe;
	
	public Ellipse(double demiGrandAxe, double demiPetitAxe) {
		super();
		this.demiGrandAxe=demiGrandAxe;
		this.demiPetitAxe=demiPetitAxe;
	}
	
	public double getDemiGrandAxe() {
		return demiGrandAxe;
	}
	
	public double getDemiPetitAxe() {
		return demiPetitAxe;
	}


	@Override
	public double calcPerimetre() {
		// TODO Auto-generated method stub
		return Math.PI*Math.sqrt(2*(demiGrandAxe*demiGrandAxe+demiPetitAxe*demiPetitAxe));
	}

	@Override
	public double calcSurface() {
		// TODO Auto-generated method stub
		return Math.PI*demiGrandAxe*demiPetitAxe;
	}
	
	public boolean equals(Object obj) {
		boolean res=false;
		if((obj!=null) && (obj instanceof Ellipse)) {
			Ellipse objEllipse=(Ellipse)obj;
			res=(objEllipse.getDemiGrandAxe()==this.demiGrandAxe&&
					objEllipse.getDemiPetitAxe()==this.demiPetitAxe);
		}
		return res;
	}
	
}
