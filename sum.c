#include <stdio.h>

int our_function(int size, int *nums)
{
  int i;
  int sum = 0;
  for(i=0; i<size; i++)
  {
    sum += nums[i];
  }
  return sum;
}

void myHello()
{
  printf("Hello!\n");
}

void myFunc(int (*f)(int, int))
{
  int a = 5, b = 10;
  printf("result a>b = %d\n", f(a, b));
}
