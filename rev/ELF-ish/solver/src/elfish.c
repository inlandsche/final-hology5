#include <ctype.h>
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <errno.h>
#include <sys/random.h>
#include <setjmp.h>
#include<elf.h>
#define FOR(var, s, e, block) {                 \
    int var;                                    \
    jmp_buf L ## var;                           \
    if ((var = setjmp(L ## var) + s) < e) {     \
      block;                                    \
      longjmp(L ## var, var - s + 1);           \
    }                                           \
  }

unsigned long long int jep(int c){
	unsigned long long int v= 0x5cd43e;
	unsigned long long int k = 0x136d43;
	unsigned long long int state = (((v^k) >> 3) & 0xffffff | (v << 1));
	unsigned long long int velov = c;
	return state * velov;
}
int main(int argc, char const *argv[])
{
	int count=0;
	unsigned long long int yeet[57] = {0x4b8fcb98, 0x50a5c811, 0x4e77c994, 0x50a5c811, 0x4ad5cc19, 0x57e9c307, 0x2681e54b, 0x595dc205, 0x3965d831, 0x50a5c811, 0x3737d9b4, 0x3737d9b4, 0x3e7bd4aa, 0x37f1d933, 0x4505d021, 0x17f9ef5f, 0x538dc60d, 0x4505d021, 0x4dbdca15, 0x2399e74f, 0x4febc892, 0x48a7cd9c, 0x25c7e5cc, 0x4505d021, 0x5447c58c, 0x52d3c68e, 0x22dfe7d0, 0x5501c50b, 0x4733ce9e, 0x4e77c994, 0x4961cd1b, 0x538dc60d, 0x50a5c811, 0x4f31c913, 0x250de64d, 0x4505d021, 0x52d3c68e, 0x4c49cb17, 0x4ad5cc19, 0x4b8fcb98, 0x5447c58c, 0x2dc5e041, 0x4505d021, 0x50a5c811, 0x52d3c68e, 0x4505d021, 0x4c49cb17, 0x538dc60d, 0x4505d021, 0x4c49cb17, 0x5447c58c, 0x4505d021, 0x250de64d, 0x58a3c286, 0x2dc5e041, 0x5ad1c103};
	//char flagger[] = "hology5{OoLLVM_!s_k1nd4_tr0ublesom3_right?_or_is_it_3z?}";
	char ip[56];
	// printf("{");
	// FOR(i,0,strlen(flagger),{
	// 	printf("0x%llx, ",jep(flagger[i]));
	// });
	// printf("}");
	puts("Welcome to the Hology5 finale! We'll begin with another flag checker (bored :(). Please input the flag!");
	scanf("%s",ip);
	FOR(i,0,56,{
		if(jep(ip[i]) == yeet[i]){
			count+=1;
		}
		else{
			count-=1;
		}
	});
	if(count == 56){
		exit(1337);
	}else{
		exit(-1);
	}
	return 0;
}