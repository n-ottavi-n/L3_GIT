package td1_ex1;

public class ConcreteStackArray implements AStack{
	
	public Object[] elements;
	private int tailleMax;
	private int tailleActuelle=0;
	
	public ConcreteStackArray(int taille) {
		tailleMax=taille;
		elements=new Object[tailleMax];
	}

	@Override  //return true si la pile est vide
	public boolean isEmpty() {
		return tailleActuelle==0;
	}

	@Override
	public void push(Object obj) {
		if(tailleActuelle<tailleMax) {
			elements[tailleActuelle]=obj;
			tailleActuelle++;
		}
		else {
			System.out.println("STACK OVERFLOW");
		}
	}
		

	@Override 
	public Object peek() {
		Object res=null;
		if(!this.isEmpty()) {
			res=elements[tailleActuelle-1];
			}		
		return res;
	}

	@Override 
	public Object pop() {
		Object res=this.peek();
		if(res!=null) {			
			elements[tailleActuelle-1]=null;
			tailleActuelle--;
		}
		return res;
	}
	
}
