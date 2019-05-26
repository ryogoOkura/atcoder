/*
 ============================================================================
 Name        : abc102maximum_difference.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
	int n,i,j,maxdif=0;
	scanf("%d*",&n);
	int a[n];
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
		for(j=0;j<i;j++){
			if(abs(a[i]-a[j])>maxdif){
				maxdif=abs(a[i]-a[j]);
			}
		}
	}
	printf("%d",maxdif);
}
