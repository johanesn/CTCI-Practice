/*
	Reverse String: implement a function void reverse (char* str) in C or C++ which reverses a null-terminated string

*/

#include <stdio.h>

#define STR_SIZE 100 

int strLength(char* str) {
	int c = 0;

	while ( *(str+c) != '\0') {
		c++;
	}

	return c; 
}

void reverse (char* str){

	printf("reversing string\n");

	int length;

	char *begin, *end, temp;

	length = strLength (str);
	begin  = str;
	end    = str;

	printf ("length: %d\n", length); 

	for (int i=0 ; i<length-1 ; i++) {
		end++; 
	}

	for (int i=0 ; i<length/2 ; i++){
		temp = *end;
		*end = *begin;
		*begin = temp;

		begin++;
		end--;
	}

}

int main() {

	char str[STR_SIZE] = "johanes";

	reverse (str);

	printf ("reversed string: %s", str);

	return 0;
} 