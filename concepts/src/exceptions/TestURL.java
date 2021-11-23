package exceptions;

import java.net.MalformedURLException;
import java.net.URL;

public class TestURL {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String urlString="https://www.universita.corsica/";
		URL u1;
		try {
			u1=new URL(urlString);
			System.out.println("la creation de l'URL s'est bien passée");			
		}catch(MalformedURLException e) {
			System.err.println("probleme lors de la creation, il semble que"+urlString+"ne soit pas un URI correct");
		}
	}

}
