package atelier2_poo;

import java.time.LocalDate;
import java.util.ArrayList;


/**
 * @author notta
 *
 */
public class Secretaire extends Employe {
	
	private ArrayList<Manager> managers;
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 * @param managers
	 */
	protected Secretaire(String leNom,String lePrenom, LocalDate laDate, Adresse lAdresse, 
			double salaire, LocalDate dateEmbauche, ArrayList<Manager> managers) {
		super(leNom,lePrenom,laDate,lAdresse, salaire, dateEmbauche);
		this.managers=managers;
	}
	
	/**
	 * @param leNom
	 * @param lePrenom
	 * @param laDate
	 * @param lAdresse
	 * @param salaire
	 * @param dateEmbauche
	 * @param managers
	 * @return null si age invalide, new secretaire sinon
	 */
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
	
	/**
	 *
	 */
	public void augmenterLeSalaire(double pourcentage) {
		if(pourcentage>0) {		
			salaire+=salaire*(pourcentage/100+(managers.size()*0.1));
		}
		else {
			System.out.println("le pourcentage doit etre positif");
		}
	}
	
	/**
	 * @param manager
	 */
	public void addManager(Manager manager) {
		managers.add(manager);
	}
	
	/**
	 * @param manager
	 */
	public void supManager(Manager manager) {
		managers.remove(manager);
	}
	
	/**
	 * Affiche la liste des managers
	 */
	public void viewManagers() {
		for (int i=0;i<managers.size();i++){
			System.out.println(managers.get(i));
		}
	}
}
