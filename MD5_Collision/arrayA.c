#include <stdio.h>

unsigned char xyz[200] = {
	[0 ... 199] = 'A'
};

int main()
{
	int i;
	for (i=0; i<200; i++){
	printf("%x", xyz[i]);
	}
	printf("\n");
}
