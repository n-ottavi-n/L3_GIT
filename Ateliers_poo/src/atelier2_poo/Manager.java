package atelier2_poo;

import java.time.LocalDate;


public class Manager extends Employe {
	
	private Secretaire secretaire;
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 */
	protected Manager(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche) {
		super(leNom, lePrenom, laDate, lAdresse, salaire, dateEmbauche);
		
	}
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 * @return  null si age invalide, new manager sinon 
	 */
	public static Manager createManager(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche){
		int age=dateEmbauche.getYear()-laDate.getYear();
		if(age>16 && age<65) {
			Manager manager=new Manager(leNom, lePrenom, dateEmbauche, lAdresse, salaire, dateEmbauche);
			return manager;
		}
		else {
			return null;
		}
		
	}
	
	/**
	 * @return
	 */
	public Secretaire getSecretaire() {
		return secretaire;
	}
	
	/**
	 * @param secretaire
	 */
	public void setSecretaire(Secretaire secretaire) {
		this.secretaire=secretaire;
	}
	
	
	/**
	 *
	 */
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*((pourcentage+calculAnnuite()*0.5)/100);
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}

	
}
