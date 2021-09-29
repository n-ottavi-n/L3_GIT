package jeu;

import java.util.ArrayList;

import elements.Case;
import elements.Obstacle;
import joueur.Joueur;
import personnage.Personnage;

public class Jeu {
	
	private String titre;
	private static final int NBJOUEURSMAX=6;
	private static final int NBCASES=50;
	private ArrayList<Joueur> listeJoueurs;
	private ArrayList<Case> cases;
	private int nbEtapes;
	private int nbObstacles;
	private static int scoreMax;
	
	public Jeu(String titre, int nbEtapes, int nbObstacles) {
		this.titre=titre;
		this.nbEtapes=nbEtapes;
		this.nbObstacles=nbObstacles;
		listeJoueurs=new ArrayList<Joueur>();
		cases=new ArrayList<Case>();
	}
	
	public void ajouterJoueur(Joueur j) {
		if (listeJoueurs.size()<=NBJOUEURSMAX) {
			listeJoueurs.add(j);
		}
	}
	
	public ArrayList<Personnage> tousLesPersos(){
		ArrayList<Personnage> res=new ArrayList();
		for(Joueur j:listeJoueurs) {//boucle a travers les elements
			ArrayList<Personnage> persos=j.getPersos();
			if(persos!=null) {
				res.addAll(persos);
			}
		}
		return res;
		
	}
	
	public void initialiserCases() {
		int nbObsEff=0;
		for(int i=0;i<NBCASES;i++) {
			int gain=(int)(Math.random()*NBCASES);
			if(gain%5==0 && nbObsEff<nbObstacles) {
				int penalite=2*gain;
				Obstacle obs= new Obstacle(penalite);
				Case newCase= new Case(obs,gain);
				cases.add(newCase);
				nbObsEff++;
			}
			else {
				Case newCase= new Case(gain);
				cases.add(newCase);
			}
		}
	}
	
	public void lancerJeu() {
		initialiserCases();
		ArrayList<Personnage> persos=tousLesPersos();
		int i=0;
		for(Personnage p: persos) {
			Case caseActuelle=cases.get(i);
			while(!caseActuelle.sansObstacle()) {
				i++;
			}
			cases.get(i).placerPersonnage(p);
		}
	}
	
	public void afficherCases() {
		for(Case c: cases) {
			System.out.println("Case "+cases.indexOf(c)+" : "+c.toString());
		}
	}
	
	public void afficherParticipants() {
		System.out.println("LISTE DES JOUEURS");
		for(Joueur j:listeJoueurs) {
			System.out.println("-------------\n"+j.toString());
		}
		
	}
	
	public void afficherResultats() {
		afficherParticipants();
		System.out.println("JEU AtelierPOO\n*******************************\nRESULTATS");
		int max=0; //init du max
		Joueur gagnant=listeJoueurs.get(0); //init du meilleur joueur
		for(Joueur j:listeJoueurs) {
			if (j.getNbPoints()>max) {
				max=j.getNbPoints();//mise a jour du max
				gagnant=j;//mise a jour du meilleur joueur
			}
		}
		System.out.println("Le gagnat est "+gagnant.getNom()+" avec "+max+" points");
		if(max>scoreMax) {
			System.out.println("Record battu: Ancien score maximum "+scoreMax);
			scoreMax=max;//update scoreMax;

		}
		Joueur.resetNbJoueurs();
	}
	
	
	
	
	


}
