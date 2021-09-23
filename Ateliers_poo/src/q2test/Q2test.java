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
		LocalDate dateNaissance=LocalDate.of(2000,2,3);
		LocalDate dateEmb=LocalDate.of(2019,2,4);
		Adresse adresse=new Adresse(11,"av","20000","aj");
		Employe e1=Employe.createEmploye(nom, prenom, dateNaissance, adresse, 2000, dateEmb);
		System.out.println(e1);
		System.out.println(e1.calculAnnuite());
		Manager m1=Manager.createManager(nom, prenom, dateNaissance, adresse, 2000, dateEmb);
		Manager m2=Manager.createManager(nom2, prenom2, dateNaissance, adresse, 2000, dateEmb);
		ArrayList<Manager> managers=new ArrayList<Manager>();
		managers.add(m1);
		managers.add(m2);
		Secretaire s1=Secretaire.createSecretaire(nom, prenom, dateNaissance, adresse, 1500, dateEmb, managers);
		m1.setSecretaire(s1);
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

	}

}
