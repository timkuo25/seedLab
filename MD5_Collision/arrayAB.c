#include <stdio.h>

unsigned char A[200] = {
	[0 ... 199] = 'A'
};

unsigned char B[200] = {
	[0 ... 199] = 'A'
};

int main()
{
	int same = 1;
	for (int i = 0; i < 200; i++){
		if(A[i] == B[i]) continue;
		else{
			same = 0;
			break;
		}
	}
	if(same == 1) printf("Some good program");
	else printf("Some bad program:");

}

