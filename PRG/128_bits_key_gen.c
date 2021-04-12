#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#define KEYSIZE 16

void main()
{
	char key[KEYSIZE];

	//printf("%lld\n", (long long) time(NULL));
	srand (time(NULL));

	/*
	for (i = 0; i< KEYSIZE; i++)
	{
		key[i] = rand() % 256;
		printf("%.2x", (unsigned char)key[i]);
	}
	*/

	FILE* f;
	f = fopen("keylist.txt","w");
	for (long long i = 1524013729; i < 1524020929; i++)
	{
		srand (i);
		for (int j = 0; j< KEYSIZE; j++)
		{
			key[j] = rand() % 256;
			fprintf(f, "%.2x", (unsigned char)key[j]);
		}
		fprintf(f, "\n");
	}
	fclose(f);
	
}
