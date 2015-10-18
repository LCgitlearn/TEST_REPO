#include <iostream>
#include <math.h>
using namespace std;
long cIs(long a, long b){
	return 1000 - a - b;
}
int main(void){
	long a = 1;
	long b = 1;
	long c = cIs(a, b);
	for(int i = 1; i <= 998; i++){
		for(int j = i; j <= 999 - i; j++){
			a = j;
			b = i;
			c = cIs(a, b);
			if(pow(a, 2) + pow(b, 2) == pow(c, 2)){
				cout << a <<
					", " <<
					b <<
					", " <<
					c << 
					" : " <<
					a*b*c
					<< endl;
				return 0;
			}
		}
	}
}
