//
//  main.cpp
//  Week 5:  Practicionum (Celcius to Farenheight)
//
//  Created by Brave Omondi on 25/09/2025.
//

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;


int main() {
   cout << fixed << setprecision(2);

    int fahrenheit;
    double celius;
   
    
    cout << setw(12) << "Fahrenheit" << setw(12) << "Celius" << endl;
    cout << "------------------------" << endl;
    for (fahrenheit = -20; fahrenheit < 120; fahrenheit +=5) {
        celius = (fahrenheit - 32) * 5/9;
        cout << setw(12) << fahrenheit << setw(12) << celius << endl;
    }
    return 0;
}
