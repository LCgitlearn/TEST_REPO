class TimeTest{
	public static void main(String[] args){
		int primeCount = 0;
		int prime;
		for(int i = 2;; i++){
			if(checkPrime(i)){
				primeCount++;
				/* System.out.println(i); */
			}
			if(primeCount >= 10001){
				prime = i;
			       	break;
			}
		}
		System.out.println(prime);
	}

	static boolean checkPrime(int num){
		for(int i = 2; i < num - 1; i++)
			if(num%i == 0) return false;
		return true;
	}
}
