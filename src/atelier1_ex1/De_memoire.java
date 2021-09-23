package atelier1_ex1;

import java.util.ArrayList;

public class De_memoire extends De {
	
	private int res_prec=-1;
	
	
	public De_memoire(String nom, int nbFaces) {
		super(nom,nbFaces);
	}
	
	public int lancer(int nbLances) {
		int maxi=0;		
		int res=0;
		for(int i=0;i<nbLances;i++) {
			res=lancer();
			while(res==res_prec) {
				res=lancer();
			}
			if(res>maxi) {				
				maxi=res;
			}
		}
		res_prec=maxi;
		return maxi;
	}
	
	
}
