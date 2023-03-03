// Find whether the given element is present or not.
// If N is 0 => Print Invalid.
/*
Input:
First Line contains integer N
Next N Lines contains array elements
Next Line contains an element to find

5
1
2
3
4
5
7

Output:
No
*/
#include<stdio.h>

int main(){
    int n,arr[50],i,flag=0,check;
    scanf("%d", &n);
    if(n == 0){
        printf("Invalid");
        return 0;
    }
    for(i = 0; i < n; i++) scanf("%d", &arr[i]);
    scanf("%d", &check);
    for(i = 0; i < n>; i++){
        if(check == arr[i]){
            flag = 1;
            break;
        }
    }
    if(flag) printf("Yes");
    else printf("No");
    return 0;
}

// Time Complexity - O(n)
// Space Complexity - O(n)