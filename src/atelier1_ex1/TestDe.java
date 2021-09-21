package atelier1_ex1;

public class TestDe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		De de1=new De(60);
		De de2=new De(30);
		String nom1=de1.getName();
		String nom2=de2.getName();
		int nb1=de1.getNbFaces();
		System.out.println("nom: "+nom1);
		System.out.println("nom: "+nom2);
		System.out.println("nb faces: "+nb1);
		int res1=de1.lancer();
		System.out.println("methode lancer1: "+res1);
		//de1.setNbFaces(2);
		int res2=de1.lancer(5);
		System.out.println("methode lancer2: "+res2);
		System.out.println(de1.toString());
		System.out.println(de1.equals(de2));
		De_Pipe depipe=new De_Pipe(40,"de_pipé", 60);
		int res3=depipe.lancer(5);
		System.out.println("lancer dé pipé: "+res3);
		}

}
