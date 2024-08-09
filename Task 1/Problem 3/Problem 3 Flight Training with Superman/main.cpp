#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>


using namespace std;

//Declaration of the Max Number function
unsigned int Max_Number(unsigned int *arr, unsigned int length);


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

    //printf("----------------------------------\n"); separator

    result = Max_Number(ARRAY, N); //call of the function

    if(1 == result){       //if condition to check for NULL pointer error
        printf("NULL Pointer!!!");
    }
    printf("%i",result);

}

//Definition of the function
unsigned int Max_Number(unsigned int *arr, unsigned int length){

    unsigned int Max = arr[0];
    unsigned index = 0;
    unsigned int Ret_Value = 0;

    if(NULL == arr){ //condition for NULL pointer
        Ret_Value = 1;
    }
    else{
        for(index; index < length; index++){ //The algorithim

            if(Max <= arr[index]){
                Max = arr[index];
                Ret_Value = Max;
            }
        }

    }

    return Ret_Value;
}
