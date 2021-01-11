import java.lang.*;

public class randomgenerator
{
	public static void main(String[] args) {
int high=6;
int low=1;
int rand = (int)(System.currentTimeMillis()%high)+low;
System.out.println(rand);

	}
}
