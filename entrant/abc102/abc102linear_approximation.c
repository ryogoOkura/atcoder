/*
 ============================================================================
 Name        : abc102linear_approximation.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

/*すぬけ君は、長さ N の整数列 Aを持っています。
 * すぬけ君は、整数bを自由に選び、
 * abs(A1−(b+1))+abs(A2−(b+2))+…+abs(AN−(b+N))
 * を計算します。
 * この最小値を求めてください。
 * bを中央値とするのが最適となる
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
	int i,j,n,sum,tmp,frag=1;
	scanf("%d",&n);
	int a[n];
	for(i=0;i<n;i++){
		scanf("%d",&a[i]);
		sum+=a[i]-i;
	}
	i=(int)sum/n-1;
	sum=0;
	for(j=0;j<n;j++)	sum+=abs(a[i]-i-j);
	i++;
	do{
		tmp=0;
		for(j=0;j<n;j++)	sum+=abs(a[i]-i-j);
		i++;
		if(sum>tmp){
			sum=tmp;
		}else frag=0;
	}while(frag);
	printf("%d",sum);
	return 0;
}
