package atelier2_poo;

import java.time.LocalDate;


public class Manager extends Employe {
	
	private Secretaire secretaire;
	
	protected Manager(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche) {
		super(leNom, lePrenom, laDate, lAdresse, salaire, dateEmbauche);
		
	}
	
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
	
	public Secretaire getSecretaire() {
		return secretaire;
	}
	
	public void setSecretaire(Secretaire secretaire) {
		this.secretaire=secretaire;
	}
	
	
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*((pourcentage+calculAnnuite()*0.5)/100);
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}

	
}
