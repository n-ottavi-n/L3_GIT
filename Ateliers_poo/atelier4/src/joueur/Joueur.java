package joueur;

import java.util.ArrayList;

import personnage.Personnage;


public class Joueur {
	
	private String nom;
	private String code="J";
	private static int nbJoueurs=0;
	private int nbPoints=0;
	private ArrayList<Personnage> listePersos;
	
	public Joueur(String nom) {
		this.nom=nom;
		nbJoueurs++;
		code+=nbJoueurs;
		listePersos=new ArrayList<Personnage>();
	}
	
	public String getNom() {
		return nom;
	}
	
	public int getNbPoints() {
		return nbPoints;
	}
	
	public void ajouterPersonnage(Personnage p) {
		listePersos.add(p);
		p.setProprietaire(this);
	}
	
	public void modifierPoints(int nb) {
		nbPoints+=nb;
	}
	
	public boolean peutJouer() {
		return listePersos.size()>0;
	}
	
	public ArrayList<Personnage> getPersos(){
		return listePersos;
	}
	
	public String toString() {
		String res=code+" "+nom+"("+nbPoints+")";
		if (peutJouer()) {
			res+=" avec "+listePersos.size()+" personnages";
		}
		else {
			res+=" aucun personnage";
		}
		return res;
	}
	
	public static void resetNbJoueurs() {
		nbJoueurs=0;
	}
	
	
	
	

}
