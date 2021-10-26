package td1_ex2;

public class Test_clone {

	public static void main(String[] args) throws CloneNotSupportedException {
		// TODO Auto-generated method stub
		UneClasse uc1=new UneClasse();
		Mere m1=new Mere(2,uc1);
		
		System.out.println(m1);
		
		
		
		Mere m2=(Mere) m1.clone();
		System.out.println(m2);
		
		System.out.println(m1.getUnObjet());
		System.out.println(m2.getUnObjet());
		
		System.out.println(m1.getI());
		System.out.println(m2.getI());




	}

}
