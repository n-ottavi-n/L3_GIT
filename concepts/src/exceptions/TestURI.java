package exceptions;

import java.net.URI;
import java.net.URISyntaxException;

public class TestURI {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		String uriString="https://www.universita.corsica/";
		URI u1;
		try {
			u1=new URI(uriString);
			System.out.println("la creation de l'URI s'est bien passée");			
		}catch(URISyntaxException e) {
			System.err.println("probleme lors de la creation, il semble que"+uriString+"ne soit pas un URI correct");
		}

	}

}
