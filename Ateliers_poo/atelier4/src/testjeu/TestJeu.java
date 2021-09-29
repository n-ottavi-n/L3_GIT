package testjeu;

import jeu.Jeu;
import joueur.Joueur;
import personnage.Humain;
import personnage.Tauren;

public class TestJeu {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		for(int i=0;i<5;i++) {
			Jeu atelierPoo=new Jeu("AtelierPOO",4,10);
			
			Joueur paul=new Joueur("paul");
			Tauren hector=new Tauren("Hector",15,10);
			Humain jean=new Humain("jean", 10);
			
			paul.ajouterPersonnage(hector);
			paul.ajouterPersonnage(jean);
			
			Joueur lucien=new Joueur("lucien");
			Tauren hercule=new Tauren("Hercule",20,5);
			Humain marie=new Humain("marie", 10);
			
			lucien.ajouterPersonnage(hercule);
			lucien.ajouterPersonnage(marie);
			
			atelierPoo.ajouterJoueur(paul);
			atelierPoo.ajouterJoueur(lucien);
			
			atelierPoo.lancerJeu();
			
			atelierPoo.afficherCases();
			
			//atelierPoo.afficherParticipants();
			
		}
		

	}

}
