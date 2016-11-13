1#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

void reverse(char* str) {
  char* tmp_str = str;
  while (*tmp_str) {
    tmp_str++;
  }

  while (str < tmp_str) {
    char tmp = *str;
    *str++ = *tmp_str;
    *tmp_str-- = tmp;
  }
}

int main() {
  char* c = (char* ) "salina";
  printf("before reverse: %s\n", c);
  reverse(c);
  printf("reversed salina: %s", c);
  return 0;
}
