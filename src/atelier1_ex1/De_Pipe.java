package atelier1_ex1;

public class De_Pipe extends De {
	
	private final int VALMIN;
	
	public De_Pipe(int valMin, String nom, int nbFaces) {
		super(nom,nbFaces);
		if (valMin>=0 && valMin<=nbFaces) {
			this.VALMIN=valMin;
		}
		else {
			this.VALMIN=0;
		}
	}
	
	public int lancer(int nbLances) {
		int maxi=VALMIN;	//borne min	
		for(int i=0;i<nbLances;i++) {			
			int res=lancer();			
			if(res>maxi) {				
				maxi=res;
			}
		}
		return maxi;
	}
	
}