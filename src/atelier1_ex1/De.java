package atelier1_ex1;

import java.util.*;

public class De {
	
	//attributs
	private String nom;
	private int nbFaces;
	public static String err="nbfaces out of range";
	private static int nbDes=1;
	private static Random r = new Random();
		
	
	//constructeurs
	public De(String nom,int nbFaces) {
		this.nom=nom;
		this.nbFaces=nbFaces;
		nbDes++;
	}
	public De() {
		this("De n°"+nbDes,6);
	}
	public De(String nom) {
		this(nom,6);
	}
	public De(int nbFaces) {
		this("De n°"+nbDes,nbFaces);
	}
	
	//methodes
	
	public int getNbFaces(){
		return nbFaces;		
	}
	
	public void setNbFaces(int nbFaces){		
		if (nbFaces>=3 && nbFaces<=120){
			this.nbFaces=nbFaces;
		}
		else {
			System.err.println(err);
		}
	}
	
	public String getName() {
		return nom;
	}
	
	public int getNbDes() {
		return nbDes;
	}
	
	public int lancer() {
		int nbAleatoire= r.nextInt(nbFaces);
		return nbAleatoire+1;
	}
	
	public int lancer(int nbLances) {
		int maxi=0;
		
		for(int i=0;i<nbLances;i++) {
			
			int res=lancer();
			
			if(res>maxi) {
				
				maxi=res;
			}
		}
		return maxi;
	}
	
}
