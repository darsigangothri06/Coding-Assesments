// Print given array in reverse order
/*
Input:
5
1 2 3 4 5

Output:
5
4
3
2
1
*/
#include<stdio.h>

int main(){
    int n,arr[50],i;
    scanf("%d", &n);
    for(i = 0; i < n; i++) scanf("%d", &arr[i]);
    for(i = n - 1; i >= 0; i--) printf("%d  ", arr[i]);
    return 0;
}

// Time Complexity - O(n)
// Space Complexity - O(n)