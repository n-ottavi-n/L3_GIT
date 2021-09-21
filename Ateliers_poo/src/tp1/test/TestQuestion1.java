package tp1.test;

import atelier2_poo.Personne;

public class TestQuestion1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String nom="nom1";
		Personne p1=new Personne(nom,"prenom1",2,3,90,11,"av","20000","aj");
		Personne p2=new Personne(nom,"prenom1",2,3,90,11,"av","20000","aj");
		Personne p3=new Personne(nom,"prenom1",2,3,90,11,"av","20000","aj");
		boolean res=p2.equals(p3);
		System.out.println(res);
		System.out.println("p1 nom == p2 nom: "+(p2.getNom()==p3.getNom()));
		System.out.println("p1 prenom == p2 prenom: "+(p2.getPrenom()==p3.getPrenom()));
	}

}
