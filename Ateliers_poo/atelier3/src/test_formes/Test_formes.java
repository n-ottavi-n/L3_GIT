package test_formes;

import java.util.ArrayList;

import formes.Forme;
import formes_2d.*;
import formes_3d.*;

public class Test_formes {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Cercle c1=new Cercle(5);
		Ellipse e1=new Ellipse(5,3);
		Rectangle r1=new Rectangle(2,4);
		Cylindre cy1=new Cylindre(2,5);
		Sphere s1=new Sphere(2);
		ArrayList formes=new ArrayList<Forme>();
		formes.add(c1);
		formes.add(e1);
		formes.add(r1);
		formes.add(cy1);
		formes.add(s1);
		for(int i=0;i<formes.size();i++) {
			System.out.println(formes.get(i));
		}
		Cercle c2=new Cercle(5);
		System.out.println(c1.equals(c2));

	}

}
