package formes_3d;

public abstract class Forme3d extends formes.Forme {
	
	
	public Forme3d() {
		super();
	}
	
	public abstract double calcVolume();
	
	public String toString() {
		return "Forme 3D "+super.toString()+" et de volume: "+calcVolume();
	}
	
}
