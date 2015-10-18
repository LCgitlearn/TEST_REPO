#include <iostream>
using namespace std;
int main(void){
	long long num = 600851475143;
	for(int i = 1; i < num; i++)
		if(num%i == 0) num /= i;
	cout << num << endl;
	
}
