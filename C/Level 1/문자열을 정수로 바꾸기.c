#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

const char* string = "-12345";

int change(const char *s, int i){
	int answer = 0;
	while(s[i] != '\0'){
			answer *= 10;
			answer += s[i]-48;
			i += 1;
		}
	return answer;	
}

int solution(const char* s) {
	
    if(s[0] == '-'){return change(s, 1) * -1;}

    else if(s[0] == '+'){return change(s, 1);}

	else{return change(s, 0);}
}

int solution2(const char* s) {
	return atoi(s);
}

void main(){
	int a;
	a = solution2(string);
	printf("%d", a);
}
