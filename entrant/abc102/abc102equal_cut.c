/*
 ============================================================================
 Name        : abc102equal_cut.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

/*すぬけ君は、長さ N の整数列 A を持っています。
 * A を 4つの（空でない）連続する部分列 B,C,D,E に分解します。
 * 整数列 B,C,D,E について、その要素の総和をそれぞれ P,Q,R,S とおきます。
 *  P,Q,R,S の最大値と最小値の差の絶対値としてあり得る最も小さい値を求めてください。
 */
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int main(void) {
	int i,j,n,max,min,tmp,cutsum[4];
	scanf("%d",&n);
	int a[n],sum[n],lcut[n],rcut[n];
	for(i=0;i<n;i++) scanf("%d",&a[i]);
	sum[0]=a[0];
	for(i=1;i<n;i++) sum[i]=sum[i-1]+a[i];
	//真ん中の切込みをa[i]とa[i+1]の間と固定したときの左右の切れ込みを考える
	lcut[1]=0;
	for(i=2;i<n-2;i++){
		lcut[i]=lcut[i-1];
		while(abs(sum[lcut[i]]-(sum[i]-sum[lcut[i]])) >
			abs(sum[lcut[i]+1]-(sum[i]-sum[lcut[i]+1]))){
			lcut[i]++;
		}
	}
	rcut[n-3]=n-2;
	for(i=n-4;i>0;i--){
		rcut[i]=rcut[i+1];
		while(abs((sum[n-1]-sum[rcut[i]])-(sum[rcut[i]]-sum[i])) >
			abs((sum[n-1]-sum[rcut[i]-1])-(sum[rcut[i]-1]-sum[i]))){
			rcut[i]--;
		}
	}
	tmp=1000000000;
	for(i=1;i<n-2;i++){
		printf("%d %d %d\n",lcut[i],i,rcut[i]);
		cutsum[0]=sum[lcut[i]];
		cutsum[1]=abs(sum[i]-sum[lcut[i]]);
		cutsum[2]=abs(sum[rcut[i]]-sum[i]);
		cutsum[3]=abs(sum[n-1]-sum[rcut[i]]);
		printf("%d %d %d %d\n",cutsum[0],cutsum[1],cutsum[2],cutsum[3]);
		max=0;
		min=cutsum[0];
		for(j=0;j<4;j++){
			if(max<cutsum[j]) max=cutsum[j];
			if(min>cutsum[j]) min=cutsum[j];
		}
		if(tmp>max-min) tmp=max-min;
	}
	printf("%d",tmp);
	return 0;
}
