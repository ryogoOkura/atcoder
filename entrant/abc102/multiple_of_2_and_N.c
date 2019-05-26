/*
 ============================================================================
 Name        : multiple_of_2_and_N.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>

int main(void) {
	int n;
	scanf("%d",&n);
	if(n%2==1){
		n*=2;
	}
	printf("%d",n);
}
