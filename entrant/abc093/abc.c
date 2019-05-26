/*
 ============================================================================
 Name        : abc.c
 Author      :
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */
/*
問題文
a,b,c からなる長さ 3の文字列Sが与えられます。
Sを abc を並び替えて作ることができるかどうか判定してください。
制約
|S|=3
Sは a,b,c からなる
*/
#include <stdio.h>
#include <stdlib.h>

int main(void) {
	char s[4];
	scanf("%s",s);
	int i,frag[3]={};
	for(i=0;i<3;i++){
		frag[s[i]-'a']++;
	}
	for(i=0;i<3;i++){
		if(frag[i]!=1){
			printf("No\n");
			break;
		}
	}
	if(i==3){
		printf("Yes\n");
	}
	return 0;
}
