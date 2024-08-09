#include <iostream>

using namespace std;

int main(){

    unsigned int Number_of_rows = 0; //get the number of rows from user
    printf("Please enter the number of rows: ");
    scanf("%d", &Number_of_rows);//save the data

    unsigned int i = 0; //iteration index of the rows
    unsigned int j = 0;//iteration index of the columns

    for(i = 1; i <= Number_of_rows; i++){ //loop on rows
        for(j = 1; j <= i; j++){ //loop on columns
            printf("*");
        }
        printf("\n"); //new line each new row
    }
}
