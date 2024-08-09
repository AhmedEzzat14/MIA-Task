#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;

//Declaration of the Searching function
unsigned int Searching(unsigned int *arr,
                       unsigned int length,
                       unsigned int Element);


int main(){

    unsigned result = 0;

    unsigned int N = 0;
    //printf("Please enter number of elements: "); get the elements of array from user
    scanf("%i", &N);

    unsigned int ARRAY[N]; //our array

    for(int i = 0; i < N; i++){ //loop to assign elements from user to array
        scanf("%i", &ARRAY[i]);
    }

    //a loop to check that the elements we get is well assigned to array
    /*for(char i = 0; i < N; i++){
        printf("%i\t", ARRAY[i]);
        printf("\n");
    }*/

    unsigned int element = 0;
    //printf("Please enter the element you want to search for: "); get the element you want to search for
    scanf("%i", &element);

    //printf("----------------------------------\n"); separator

    result = Searching(ARRAY, N, element); //call of the function

    if(1 == result){       //if condition to check for NULL pointer error
        printf("NULL Pointer!!!");
    }
    else if(-1 == result){ //condition if the element not exist
        printf("-1");
    }


}

//Definition of the function
unsigned int Searching(unsigned int *arr,
                       unsigned int length,
                       unsigned int Element){

    unsigned int Ret_Value = 0;
    unsigned index = 0;

    if(NULL == arr){ //condition for NULL pointer
        Ret_Value = 1;
    }
    else{
        for(index; index < length; index++){ //Searching algorithim

            if(arr[index] == Element){
                printf("%i", index);
                Ret_Value = 0;
                break;
            }
            else{
                Ret_Value = -1;
            }
        }

    }

    return Ret_Value;
}
