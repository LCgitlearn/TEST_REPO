import java.util.ArrayList;
class p12{
	public static void main(String[] args){
		int count = 0;
		for(int i = 0;;){
			count += ++i;
			if(yakusuNum(count) > 500){
				System.out.println(count);
				break;
			}
		}
	}

	static int yakusuNum(int num){
		ArrayList<Integer> yakusu = new ArrayList<Integer>();
		double maxLoop = Math.sqrt(num);
		if(num == 0) return 0;
		if(num == 1) return 1;
		for(int i = 2; i <= maxLoop; i++){
			if(num%i == 0){
				yakusu.add(i);
				if(i == maxLoop)
					return yakusu.size() * 2 + 1;
			}
		}
		return yakusu.size() * 2 + 2;
	}
}
