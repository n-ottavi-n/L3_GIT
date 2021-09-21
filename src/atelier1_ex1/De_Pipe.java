package atelier1_ex1;

public class De_Pipe extends De {
	
	private int valMin;
	
	public De_Pipe(int valMin, String nom, int nbFaces) {
		super(nom,nbFaces);
		if (valMin>=0 && valMin<=nbFaces) {
			this.valMin=valMin;
		}
		else {
			this.valMin=0;
		}
	}
	
	public int lancer(int nbLances) {
		int maxi=valMin;		
		for(int i=0;i<nbLances;i++) {			
			int res=lancer();			
			if(res>maxi) {				
				maxi=res;
			}
		}
		return maxi;
	}
	
}
