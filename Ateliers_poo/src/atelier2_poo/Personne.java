package atelier2_poo;

import java.time.LocalDate;


public class Personne{
    private static final Adresse ADRESSE_INCONNUE = null;
    private static int nbPersonnes=0;
    private String nom;
    private String prenom;
    private final LocalDate dateNaissance;
    private Adresse adresse=ADRESSE_INCONNUE;
	
	/**
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param laDate la date de naissance de la personne
	 * @param lAdresse l'adresse de la personne
	 */
	public Personne(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse){
		nom = leNom.toUpperCase();
		prenom=lePrenom;
		dateNaissance=laDate;
		adresse=lAdresse;
		nbPersonnes++;
	}
	
	/** 
	 * Constructeur de Personne
	 * @param leNom le nom de la personne
	 * @param lePrenom le prénom de la personne
	 * @param j le jour de naissance
	 * @param m le mois de naissance
	 * @param a l'année de naissance
	 * @param numero le n° de la rue
	 * @param rue la rue
	 * @param code_postal le code postal de l'adresse
	 * @param ville la ville ou la personne habite
	 */
	public Personne(String leNom,String lePrenom, int j, int m, int a, int numero, String rue, String code_postal, String ville){
		this(leNom, lePrenom, LocalDate.of(a,m,j),new Adresse(numero,rue,code_postal,ville));
	}

	/**
	 * Accesseur
	 * @return retourne le nom
	 */
	public String getNom(){
		return nom;
	}
	/**
	 * Accesseur
	 * @return retourne le prénom
	 */
	public String getPrenom(){
		return prenom;
	}
	/**
	 * Accesseur
	 * @return retourne la date de naissance	 
	 */
	public LocalDate getDateNaissance() {
		return dateNaissance;
	}
	/**
	 * Accesseur
	 * @return retourne l'adresse	 
	 */
	public Adresse getAdresse() {
		return adresse;
	}
	/**
	 * Modificateur
	 * @param retourne l'adresse	 
	 */
	public int getNbPersonnes() {
		return nbPersonnes;
	}
	
	public void setAdresse(Adresse a) {
		adresse=a;
	}
		
	/* (non-Javadoc)
	 * @see java.lang.Object#toString()
	 */
	
	public static boolean plusAgee(Personne p1, Personne p2) {
		return p1.getDateNaissance().isAfter(p2.getDateNaissance());
	}
	
	public boolean plusAgeeQue(Personne personne) {
		return personne.getDateNaissance().isAfter(this.dateNaissance);
	}
		
	public String toString(){
		String result="\nNom : "+nom+"\n"
		+"Prénom : "+prenom+"\n"+
		"Né(e) le : "+dateNaissance.getYear()+
		"-"+dateNaissance.getMonthValue()+
		"-"+dateNaissance.getDayOfMonth()+"\n"+
		"Adresse : "+
		adresse.toString();
		return result;
	}
	
	public boolean equals(Object obj) {
		boolean res=false;
		if(obj instanceof Personne) {
			Personne objPersonne=(Personne)obj;
			res=(objPersonne.getNom()==this.nom && objPersonne.getPrenom()==this.prenom);
		}
		return res;
	}
}

    
   
   