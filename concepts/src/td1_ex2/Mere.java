package td1_ex2;

public class Mere implements Cloneable {
	
	private int i;
	private UneClasse unObjet; //Clonable
	
	public Mere(int unI, UneClasse unObj){
		i = unI; unObjet = unObj;
	}
	
	public int getI() {
		return i;
	}
	
	public UneClasse getUnObjet() {
		return unObjet;
	}
	
	public void setObj(UneClasse obj) {
		unObjet=obj;
	}
	
	public Object clone() throws CloneNotSupportedException {
		Mere m=null;
		UneClasse uc=(UneClasse)super.clone();
		m.setObj(uc);
		return m;
	}


}
