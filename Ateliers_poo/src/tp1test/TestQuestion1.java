package tp1test;

import atelier2_poo.*;
import java.util.*;

public class TestQuestion1 {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String nom="nom1"; 
		String prenom="prenom1";
		String nom2="nom2";
		String prenom2="prenom2";
		GregorianCalendar dateNaissance=new GregorianCalendar(1990,3,2);
		GregorianCalendar dateEmb=new GregorianCalendar(2019,3,2);
		Adresse adresse=new Adresse(11,"av","20000","aj");
		Personne p1=new Personne(nom,prenom,2,3,1990,11,"av","20000","aj");
		Personne p2=new Personne(nom,prenom,2,3,90,11,"av","20000","aj");
		//boolean res=p1.equals(p2);
		//System.out.println(res);
		//System.out.println(p2.getNom());
		//System.out.println(p1.getNom());
		//System.out.println("p1 nom == p2 nom: "+(p1.getNom()==p2.getNom()));
		//System.out.println("p1 prenom == p2 prenom: "+(p1.getPrenom()==p2.getPrenom()));	
		System.out.println(p1);
		
		
		
		
	}
}
