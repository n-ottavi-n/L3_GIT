package exceptions;

public class TestDe {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		De d1=new De(6,"d1");
		De d2=null;
		try {
			d2=new De(200,"d2");
		}catch(IllegalArgumentException e) {
			e.printStackTrace();
		}
		System.out.println(d1);
		System.out.println(d2);
		

		

	}

}
