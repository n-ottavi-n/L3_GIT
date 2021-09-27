package atelier2_poo;

import java.time.LocalDate;


public class Employe extends Personne {
	
	public double salaire;
	private LocalDate dateEmbauche;
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 */
	protected Employe(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche) {
		super(leNom,lePrenom,laDate,lAdresse);
		this.salaire=salaire;
		this.dateEmbauche=dateEmbauche;	
	}
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 * @return null si age inavlide, new employe sinon
	 */
	public static Employe createEmploye(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche){
		int age=dateEmbauche.getYear()-laDate.getYear();
		if(age>16 && age<65) {
			Employe employe=new Employe(leNom, lePrenom, dateEmbauche, lAdresse, salaire, dateEmbauche);
			return employe;
		}
		else {
			return null;
		}
		
	}
	
	/**
	 * @param pourcentage
	 */
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*(pourcentage/100);
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}
	
	/**
	 * @return simple difference des années
	 */
	public int calculAnnuite() {
		LocalDate now=LocalDate.now();
		return now.getYear()-dateEmbauche.getYear();
	}

}
