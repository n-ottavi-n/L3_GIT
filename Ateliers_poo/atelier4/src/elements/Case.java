package elements;

import personnage.Personnage;

public class Case {
	
	private int gain;
	private Personnage perso=null;
	private Obstacle obs;
	
	public Case(Obstacle obs, int gain) {
		this.obs=obs;
		this.gain=gain;
	}
	
	public Case(int gain) {
		this(null,gain);
	}
	
	public int getGain() {
		return gain;
	}
	
	public int getPenalite() {
		int res=0;
		if(obs!=null) {
			res=obs.getPenalite();
		}
		return res;
	}

	
	public void placerPersonnage(Personnage p) {
		perso=p;
	}
	
	public void placerObstacle(Obstacle o) {
		obs=o;
	}
	
	public void enleverPersonnage() {
		perso=null;
	}
	public boolean sansObstacle() {
		return (obs==null);
	}
	
	public boolean sansPerso() {
		return(perso==null);
	}
	
	public boolean estLibre() {
		return(sansObstacle() && sansPerso());
	}
	
	public String toString() {
		String res="";
		if(estLibre()) {
			res="Libre (gain = "+gain+")";
		}
		else if(!sansObstacle()) {
			res="Obstacle (penalite = "+(-gain)+")";
		}
		else if(!sansPerso()) {
			res=perso.toString()+" (penalite = "+(-gain)+")";
		}
		
		return res;
		
	}
	
	
	
	

}
