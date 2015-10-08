import java.util.*;
class Hello{
	public static void main(String[] args){
		char[] word = {'H', 'e', 'l', 'l', 'o', ',',
			' ', 'w', 'o', 'r', 'l', 'd', '!'};
		Arrays.asList(word).forEach(System.out::println);
	}
}
