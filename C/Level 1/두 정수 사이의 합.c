#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
long long solution(int a, int b);

void main(){
	int c, d;
	c = -5, d = 3;
	long long result;
	result = solution(c,d);
	printf("%d", result);
}


long long solution(int a, int b) {
    int answer = 0;
    int i;
    if(b >= a){
    	for(i=a;i<=b;i++)
    	answer += i;
	}
    else{
    	for(i=b;i<=a;i++)
    	answer += i;
	}
    return answer;
}
