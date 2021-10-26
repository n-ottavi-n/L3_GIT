package td1_ex2;

public class UneClasse implements Cloneable {
	
	
	public Object clone() {
		Object o = null;
		try {
			o=super.clone();
		} catch (CloneNotSupportedException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
		return o;
	}
	

}
