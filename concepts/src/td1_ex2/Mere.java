package td1_ex2;

public class Mere implements Cloneable {
	
	private int i;
	private UneClasse unObjet; //Clonable
	
	public Mere(int unI, UneClasse unObj){
		i = unI; unObjet = unObj;
	}
	
	public Object clone() throws CloneNotSupportedException {
		return super.clone();
	}


}
