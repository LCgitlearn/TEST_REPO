#include <iostream>
using namespace std;
bool checkPrime(int num){
	for(int i = 2; i < num - 1; i++)
		if(num%i == 0) return false;
	return true;
}
int main(void){
	int primeCount = 0;
	int prime;
	for(int i = 2;; i++){
		if(checkPrime(i)){
			primeCount++;
			// cout << i << endl;
		}
		if(primeCount >= 10001){
			prime = i;
			break;
		}
	}
	cout << prime << endl;
}
