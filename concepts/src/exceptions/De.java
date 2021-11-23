/*
 * De
 *
 * Version 1
 *
 * Date 2020/09
 *
 * Copyright notice : none
 */

// Zone des imports
package exceptions;
/*Avancée du codage à la fin de journée du
 *Jeudi 24 Septembre 2020, Atelier 1 POO
 */

//Zone des imports
import java.util.*;

public class De {

    /*Constantes de classe
      static : "de classe"
      final : " constant"
      static final : constante de classe
    */
    public static final int NB_MIN_FACES = 3;
    public static final int NB_MAX_FACES = 120;
    public static final int NB_DEFAUT_FACES = 6;
    public static final String NOM_DEFAUT = "Dé";

    //Variables de classe, elles sont rattachées à la classe, un seul espace mémoire pour la classe
    //En premier les variables public, ensuite les protected, package (pas de modificateur) enfin les private
    public static Random rand = new Random(); // On souhaite utiliser le même générateur aléatoire
    //  pour tous les dés
    private static int nbDe = 0; //On souhaite conserver le nombre de dés qui ont été créés

    /*
     * Variables (attribut, champs, etc.) d'instances, elles caractérisent une
     * instance de Dé en particulier. Chaque instance a sa propre zone mémoire
     * dédiée
     * En premier les variables public, ensuite les protected, package (pas de modificateur) enfin les private
     *
     * Concept de l'encapsulation, on va utiliser un modificateur d'accès parmi
     * les quatres possibles
     * - public : on peut accéder à l'item depuis toutes les classes
     * - protected : on peut accéder à l'item depuis les classes dérivées et les classes du même package
     * - private : l'item est seulement accessible depuis l'intérieur de la classe où il est défini.
     * -(par défaut/rien) sans modificateur d'accès, seules les classes du même package peuvent accéder à l'item.
     */

    private int nbFaces; // On le déclare privé pour le protéger, car sa modification demande
                        // de respecter certaines règles (>= NB_MIN_FACES = 3 et <= NB_MAX_FACES = 120)
    private String nom;  // On le déclare privé pour le protéger, il ne doit pas pouvoir être modifié une fois
    // affecté depuis le constructeur
    //On aurait aussi pu déclarer l'attribut nom
    //public final nom;  auquel cas on a pas besoin de méthode getNom()


    //Constructeurs
    //On écrit le constructeur le plus complet c'est à dire avec tous les paramètres nécessaires
    public De(int nFaces, String pnom) throws IllegalArgumentException,NullPointerException {    	
    	this.setNbFaces(nFaces);
        if ((pnom == null)) {
        	throw new NullPointerException("name is null");
            
        }
        else if((pnom == "")) {
        	throw new IllegalArgumentException("name is the empty string");
        }
        else {
        	nom = pnom;
        }
    }
    //On appel le constructeur le plus complet pour définir les constructeurs ayant moins de paramètres
    public De() {
        this(NB_DEFAUT_FACES,NOM_DEFAUT);
    }


    //Acesseurs et modificateurs : getter et setter
    //Accesseurs
    public int getNbFaces() {
        return nbFaces;		//Equivalent à this.nbFaces, this représente l'instance courante, celle sur
        //laquelle on invoque la méthode
    }

    public String getNom() {
        return nom;			//Equivalent à this.nom, this représente l'instance courante, celle sur
        //laquelle on invoque la méthode
    }

    //Modificateurs
    public void setNbFaces(int nvNbFaces) {
        if ((nvNbFaces >= NB_MIN_FACES) && (nvNbFaces <= NB_MAX_FACES)) {
            nbFaces = nvNbFaces;
        }else {
        	throw new IllegalArgumentException("Attention le nombre de faces doit être compris entre "+
                    NB_MIN_FACES+" et " + NB_MAX_FACES);
        }
    }

    public static int getNbDesCrees(){
        return nbDe;
    }

    //Méthodes d'instances
    //Question 5 : lancé de dé
    public int lancer() {
        return 1+rand.nextInt(nbFaces);
    }

    public int lancer(int nbLances){
        int result=lancer();
        int temp;
        for (int i=0;i<nbLances-1;i++) {
            temp = lancer();
            if (result>temp){
                result = temp;
            }
        }
        return result;
    }


    /* Methodes héritées de la classe Object
       Redefinition de la methode toString. Cette méthode par défaut renvoie l'adresse de l'objet
       en mémoire. Il faut s'astreindre à systématiquement la redéfinir pour renvoyer une description
       de l'objet sous forme de chaine de caractère.
       Elle est implicitement invoquée lorsqu'on passe une référence à un objet en paramètre de la
       méthode print. Ainsi System.out.printl(monInstance.toString()) est équivalent à
       System.out.printl(monInstance)
     */
    public String toString() {
        return "un Dé nommé " + nom + " à " + nbFaces + " faces";
    }
}
