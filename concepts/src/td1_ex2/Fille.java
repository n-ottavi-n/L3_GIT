package td1_ex2;

public class Fille extends Mere{
	
	private Object unObjetSensible;
	
	public Fille(int unI, UneClasse unObj, Object unObjSens){
		super(unI,unObj);
		setUnObjetSensible(unObjSens);
	}
	
	public Object clone()  throws CloneNotSupportedException {
		throw new CloneNotSupportedException();
	}

	public Object getUnObjetSensible() {
		return unObjetSensible;
	}

	public void setUnObjetSensible(Object unObjetSensible) {
		this.unObjetSensible = unObjetSensible;
	}
}
