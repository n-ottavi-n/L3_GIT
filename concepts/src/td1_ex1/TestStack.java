package td1_ex1;

public class TestStack {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		ConcreteStackArray csa1=new ConcreteStackArray(5);
		Integer a=5;
		Integer b=4;
		Integer c=3;
		
		System.out.println(csa1.isEmpty());

		csa1.push(a);
		csa1.push(b);
		csa1.push(c);

		System.out.println(csa1.peek());
		
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());


		ConcreteStackList csa2=new ConcreteStackList();
		
		System.out.println(csa1.isEmpty());
		
		csa1.push(a);
		csa1.push(b);
		csa1.push(c);

		System.out.println(csa1.peek());
		
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());
		System.out.println(csa1.pop());

	}

}
