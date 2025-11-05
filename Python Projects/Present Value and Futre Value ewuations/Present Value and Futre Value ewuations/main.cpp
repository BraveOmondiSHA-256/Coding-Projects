//
//  main.cpp
//  Present Value and Futre Value ewuations
//
//  Created by Brave Omondi on 02/10/2025.
//

#include <iostream>
#include <cmath>
#include <cctype>
using namespace std;


int main() {
    
    double presentValue;
    double futreValue;
    double interestRate;
    string whichCalculation;
    int numberYears;
    
    cout << "What do you want to work out? " << endl;
    cin >> whichCalculation;
    cout << endl;
    
    while (false) {
        (whichCalculation != "future value");
        if(whichCalculation != "future value"){
            cout << "Invalid" << endl;
        }
        else if((whichCalculation == "future value")){
                cout << "Give me the Present value" << endl;
                cin >> presentValue;
                cout << "Give me the interest rate" << endl;
                cin >> interestRate;
                cout << "Give me the number of years" << endl;
                cin >> numberYears;
                
                futreValue = presentValue * pow(1 + interestRate, numberYears);
                cout << "Your futre value is " << futreValue << endl;
            }
    }
    
  
    
    
    
    return 0;
}
