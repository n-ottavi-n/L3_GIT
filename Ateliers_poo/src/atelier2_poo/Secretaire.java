package atelier2_poo;

import java.time.LocalDate;
import java.util.ArrayList;


public class Secretaire extends Employe {
	
	private ArrayList<Manager> managers;
	
	protected Secretaire(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche, ArrayList<Manager> managers) {
		super(leNom,lePrenom,laDate,lAdresse, salaire, dateEmbauche);
		this.managers=managers;
	}
	
	public static Secretaire createSecretaire(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche, ArrayList<Manager> managers){
		int age=dateEmbauche.getYear()-laDate.getYear();
		if(age>16 && age<65) {
			Secretaire secretaire=new Secretaire(leNom, lePrenom, dateEmbauche, lAdresse, salaire, dateEmbauche,
				managers);
			return secretaire;
		}
		else {
			return null;
		}
		
	}
	
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*(pourcentage/100+(managers.size()*0.1));
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}
	
	public void addManager(Manager manager) {
		managers.add(manager);
	}
	
	public void supManager(Manager manager) {
		managers.remove(manager);
	}
	
	public void viewManagers() {
		for (int i=0;i<managers.size();i++){
			System.out.println(managers.get(i));
		}
	}
}
