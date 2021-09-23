package atelier2_poo;

import java.time.LocalDate;


public class Employe extends Personne {
	
	public double salaire;
	private LocalDate dateEmbauche;
	
	protected Employe(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche) {
		super(leNom,lePrenom,laDate,lAdresse);
		this.salaire=salaire;
		this.dateEmbauche=dateEmbauche;	
	}
	
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
	
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*(pourcentage/100);
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}
	
	public int calculAnnuite() {
		LocalDate now=LocalDate.now();
		return now.getYear()-dateEmbauche.getYear();
	}

}
