/*
 ============================================================================
 Name        : sameinteger.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */
/*
問題文
3つの整数 A,B,Cが与えられます。以下の 2種類の操作を好きな順で繰り返して A,B,C
をすべて等しくするために必要な操作の最小回数を求めてください。

A,B,Cのうち2つを選んで、その両方を 1増やす
A,B,Cのうち1つを選んで、その整数を2増やす

制約
0≤A,B,C≤50
入力はすべて整数である
*/
#include <stdio.h>
#include <stdlib.h>

void check(int *str,int count){
	int i,j,temp;
	if((str[0]==str[1])&&(str[1]==str[2])){
		printf("%d\n",count);
	}else{
		for(i=0;i<2;i++){
			for(j=i+1;j<3;j++){
				if(str[i]<str[j]){
					temp=str[i];
					str[i]=str[j];
					str[j]=temp;
				}
			}
		}
		if(str[0]==str[1]){
			str[2]+=2;
			check(str,count+1);
		}else{
			if(str[1]==str[2]){
				str[0]--;
				check(str,count+1);
			}else{
				str[2]+=2;
				check(str,count+1);
			}
		}
	}
}

int main(void) {
	int str[3];
	scanf("%d %d %d",&str[0],&str[1],&str[2]);
	check(str,0);
	return 0;
}
