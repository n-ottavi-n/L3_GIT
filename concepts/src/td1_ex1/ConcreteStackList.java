package td1_ex1;

import java.util.ArrayList;

public class ConcreteStackList implements AStack{
	
	public ArrayList<Object> elements;
	
	public ConcreteStackList() {
		elements=new ArrayList<Object>();
	}

	@Override  //return true si la pile est vide
	public boolean isEmpty() {
		boolean res=false;
		if(elements.size()==0) {
			res=true;
		}
		return res;
	}

	@Override
	public void push(Object o) {
		elements.add(o);		
	}

	@Override 
	public Object peek() {
		Object res=null;
			if(!this.isEmpty()) {
				res=elements.get(-1);
			}		
		return res;
	}

	@Override 
	public Object pop() {
		Object res=null;
		if(!this.isEmpty()) {			
			res=elements.remove(-1);
		}
		return res;
	}
	
	
	
}