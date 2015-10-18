#include <iostream>
#include <math.h>
using namespace std;
int main(void){
	int num = 100;
	long long result1 = 0;
	long long result2 = 0;
	for(int i = 1; i <= num; i++){
		result1 += (long)pow(i, 2);
		result2 += i;
		cout << result1 << " : " << result2 << ", " << (long)pow(result2, 2);
		cout << "\t\t" << (long)pow(result2, 2) - result1 << endl;
	}
	cout << (long)pow(result2, 2) - result1 << " : " << (long)pow(result2, 2) << " - " << result1 << endl;
}
