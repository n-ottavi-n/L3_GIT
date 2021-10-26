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
	
	public void setI(int i) {
		this.i=i;
	}
	
	public void setObj(UneClasse obj) {
		unObjet=obj;
	}
	
	public Object clone(){
		Mere m=null;
		try {
			m = (Mere)super.clone();
		} catch (CloneNotSupportedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		m.unObjet=(UneClasse)unObjet.clone();
		m.i=i;
		return m;
	}


}
