import java.util.*;
class Hello{
	public static void main(String[] args){
		Character[] word = {'H', 'e', 'l', 'l', 'o', ',',
			' ', 'w', 'o', 'r', 'l', 'd', '!'};
		List<Character> chList = Arrays.asList(word);
		chList.forEach(System.out::println);
	}
}
