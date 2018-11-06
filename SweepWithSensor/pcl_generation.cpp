#include <iostream>
#include <cstdio>
int main() 
{
    FILE *uno;
    char port[30];
    int i,data[5];

    std::cout << "enter port:";
    std::cin >> port;
    std::cout <<port <<"\n";
    uno = fopen(port,"w");
    for(i = 0; i < 3; i++){
        fprintf(uno,"%d",data[i]);
        //sleep(2);
    }
    return 0;
}