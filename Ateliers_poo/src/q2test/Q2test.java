package q2test;

import java.time.LocalDate;
import java.util.ArrayList;

import atelier2_poo.*;


public class Q2test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String nom="nom1"; 
		String prenom="prenom1";
		String nom2="nom2";
		String prenom2="prenom2";
		String nom3="nom3";
		String prenom3="prenom3";
		
		LocalDate dateNaissance=LocalDate.of(2000,2,3);
		LocalDate dateEmb=LocalDate.of(2019,2,4);
		
		Adresse adresse=new Adresse(11,"av","20000","aj");
		Employe e1=Employe.createEmploye(nom, prenom, dateNaissance, adresse, 2000, dateEmb);
		//System.out.println(e1);
		//System.out.println(e1.calculAnnuite());
		Secretaire s1=Secretaire.createSecretaire(nom, prenom, dateNaissance, adresse, 1500, dateEmb);
		Secretaire s2=Secretaire.createSecretaire(nom2, prenom2, dateNaissance, adresse, 1500, dateEmb);

		
		Manager m1=Manager.createManager(nom, prenom, dateNaissance, adresse, 2000, dateEmb,s1);
		Manager m2=Manager.createManager(nom2, prenom2, dateNaissance, adresse, 2000, dateEmb,s1);
		Manager m3=Manager.createManager(nom3, prenom3, dateNaissance, adresse, 2000, dateEmb,s1);
		//s1 a 3 manangers
		System.out.println("~~~~~~~~~~");
		s1.viewManagers();
		System.out.println("~~~~~~~~~~");
		
		m1.setSecretaire(s2);//on affecte s2 a m1; s1 a 2 manangers maintenant(m2 et m3)
		
		System.out.println("~~~~~~~~~~");
		s1.viewManagers();
		System.out.println("~~~~~~~~~~");
		
		s2.addManager(m3); //on rajoute m3 a s2, s1 a un seul manager maintenant(m2)
		
		System.out.println("~~~~~~~~~~");
		s1.viewManagers();
		System.out.println("~~~~~~~~~~");
		
		System.out.println("~~~~~~~~~~");
		s2.viewManagers(); //s2 doit avoir 2 managers(m1 et m3)
		System.out.println("~~~~~~~~~~");

/**
		ArrayList<Manager> managers=new ArrayList<Manager>();
		
		managers.add(m1);
		managers.add(m2);
	
		//Test ajout secretaire
		m3.setSecretaire(s1);
		System.out.println("~~~~~~~~~~");
		s1.viewManagers();
		System.out.println("~~~~~~~~~~");

		test augmentation de salaire
		for(int i=0;i<managers.size();i++) {
			System.out.println(managers.get(i).salaire);
		}
		m1.augmenterLeSalaire(10);
		m2.augmenterLeSalaire(10);
		for(int i=0;i<managers.size();i++) {
			System.out.println(managers.get(i).salaire);
		}
		int age=dateEmb.compareTo(dateNaissance);
		System.out.println(age);

	*/
	}

}
