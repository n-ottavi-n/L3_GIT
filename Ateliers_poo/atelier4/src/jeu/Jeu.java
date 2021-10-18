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
		for(Joueur j:listeJoueurs) {//boucle a travers les joueurs
			ArrayList<Personnage> persos=j.getPersos(); //recupere tous les persos d'un joueur
			if(persos!=null) {
				res.addAll(persos); //les ajoute a la liste
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
		//initialisation
		initialiserCases();
		ArrayList<Personnage> persos=tousLesPersos();
		int i=0;
		for(Personnage p: persos) {
			Case caseActuelle=cases.get(i);
			while(!caseActuelle.estLibre()) { 
				i++;
				caseActuelle=cases.get(i);
			}
			cases.get(i).placerPersonnage(p);
			p.deplacer(i, 0);
			
			i++;
		}
		afficherCases();
		//mouvements
		for(int j=0;j<=nbEtapes;j++) {
			for(Personnage p: persos) {
				int posNext=p.positionSouhaite();
				if(posNext>=NBCASES) { //si depassement
					posNext=NBCASES-1;
				}
				Case caseNext=cases.get(posNext);	//recupere la case ou on souhaite aller		
				if(caseNext.estLibre()) { //case destination vide
					int gain=caseNext.getGain();
					cases.get(p.getPosition()).enleverPersonnage(); //retire le perso de sa case actuelle
					p.deplacer(posNext, gain); //mets a jour la position et prend les gains
					caseNext.placerPersonnage(p); //place le perso dans la nouvelle case
				}
				else if(!caseNext.sansObstacle()) { //case destination a un obstacle
					p.penaliser(caseNext.getPenalite());
				}
				else if(!caseNext.sansPerso()){
					p.penaliser(caseNext.getGain());
				}
				//afficherCases();
			}
			//afficherCases();
		
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
		System.out.println("Le gagnant est "+gagnant.getNom()+" avec "+max+" points");
		if(max>scoreMax) {
			System.out.println("Record battu: Ancien score maximum "+scoreMax);
			scoreMax=max;//update scoreMax;

		}
		Joueur.resetNbJoueurs();	
		for(Joueur j:listeJoueurs) {
			j.resetScore();
		}
	}
	
	
	
	
	


}
