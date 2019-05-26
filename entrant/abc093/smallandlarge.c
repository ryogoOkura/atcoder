/*
 ============================================================================
 Name        : smallandlarge.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */
/*
問題文
以下を満たす整数をすべて昇順に出力してください。
A以上B以下の整数の中で、小さい方からK番目以内であるか、大きい方からK番目以内である
制約
1≤A≤B≤10^9
1≤K≤100
入力はすべて整数である
*/
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	long int a,b,i;
	int k;
	scanf("%ld %ld %d",&a,&b,&k);
	i=a;
	while(i<=b){
		printf("%ld\n",i);
		i++;
		if((i>a+k-1)&&(i<b-k+1)){
			i=b-k+1;
		}
	}
	return 0;
}
