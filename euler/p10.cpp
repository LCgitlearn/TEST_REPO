#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
vector<int> v{2, 3};
bool checkPrime(int num){
	if(num == 0 || num == 1) return false;
	int maxLoop = sqrt(num);
	for(int i: v){
		if(i > maxLoop) return true;
		if(num%i == 0) return false;
	}
	return true;
}
int main(void){
	long long result = 0;
	for(int i = 0; i < 2000000; i++){
		if(checkPrime(i)){
			v.push_back(i);
			result += i;
		}
	}
	cout << result;
}
