package td1_ex1;

import java.util.ArrayList;
import java.util.List;

public class ConcreteStackArray implements AStack{
	
	public Object[] elements;
	private int taille;
	int i=0;
	
	public ConcreteStackArray(int taille) {
		this.taille=taille;
		Object[] elements=new Object[taille];
	}

	@Override  //return true si la pile est vide
	public boolean isEmpty() {
		boolean res=false;
		if(elements==null) {
			res=true;
		}
		return res;
	}

	@Override
	public void push(Object o) {
			elements.
			i++;
	}
		

	@Override 
	public Object peek() {
		Object res=null;
			if(!this.isEmpty()) {
				res=elements[-1];
			}		
		return res;
	}

	@Override 
	public Object pop() {
		Object res=this.peek();
		if(res!=null) {			
			elements[-1]=null;
		}
		return res;
	}
	
	
	
}
