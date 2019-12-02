#include <stdio.h>

int add(int *a, int *b)
{
    return *a + *b;
}

void sum(int *arr, int size, int *out)
{
    for (int i = 0; i < size; i++)
    {
        *out += arr[i];
    }
}


int main()
{
    // int a = 1;
    // int b = 2;
    // printf("%d\n", add(&a, &b));

    // int arr[5] = {1, 2, 3, 4, 5};
    // int out = 0;
    // sum(arr, 5, &out);
    // printf("%d\n", out);

    int i = 5;
    int *p = &i;
    printf("i = %d\n", i);
    printf("p = %p\n", p);
    printf("*p = %d\n", *p);
}
