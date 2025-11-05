//
//  main.cpp
//  Week 9 - Practiciunum
//
//  Created by Brave Omondi on 23/10/2025.
//

#include <iostream>
using namespace std;

int main() {
   
    string Fizz = "Fizz";
    string Buzz = "Buzz";
    string FizzBuzz = "FizzBuzz";
    const int MAX_NUMB = 100;
    
    
    for(size_t i = 1; i < MAX_NUMB + 1; ++i){
        if(i % 3 == 0 && i % 5 == 0){
            cout << FizzBuzz << endl;
            continue;
        }
        if(i % 3 == 0){
            cout << Fizz << endl;
            continue;
        }
        if(i % 5 == 0){
            cout << Buzz << endl;
            continue;
        }
        else{
            cout << i << endl;
            continue;
        }
    }
    
    
    return 0;
}
