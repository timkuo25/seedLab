#include <stdio.h>
#include <openssl/bn.h>
#define NBITS 256
void printBN(char *msg, BIGNUM * a)
{
	/* Use BN_bn2hex(a) for hex string
	* Use BN_bn2dec(a) for decimal string */
	char * number_str = BN_bn2hex(a);
	
	printf("%s %s\n", msg, number_str);
	OPENSSL_free(number_str);
}

int main ()
{
	BN_CTX *ctx = BN_CTX_new();
	BIGNUM *e = BN_new();
	BIGNUM *n = BN_new();
	BIGNUM *d = BN_new();
	BIGNUM *m = BN_new();
	BIGNUM *s = BN_new();
	BIGNUM *verified_s = BN_new();


	BN_hex2bn(&m, "4C61756E63682061206D697373696C652E");
	BN_hex2bn(&s, "643D6F34902D9C7EC90CB0B2BCA36C47FA37165C0005CAB026C0542CBDB6802F");
	BN_hex2bn(&n, "AE1CD4DC432798D933779FBD46C6E1247F0CF1233595113AA51B450F18116115");
	BN_hex2bn(&e, "010001");

	BN_mod_exp(verified_s, s, e, n, ctx);

	printBN("m = ", m);
	printBN("verified_s = ", verified_s);

	return 0;
}

