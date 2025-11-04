/*
 * Author: Brave Omondi
 * Assignment Title: (Week 3) Practicanum -
 * Assignment Description:
 * Due Date:01/01/2025
 * Date Created:01/01/2025
 * Date Last Modified:01/01/2025
 */

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    
    int leapYear;
   
    cout << "Enter a leap year: ";
    cin >>  leapYear;
    
    if((leapYear % 4 == 0 && leapYear % 100 != 0) || (leapYear % 400 == 0)){
        cout << leapYear << " is a leap year." << endl;
    }
    else{
        cout << leapYear << " is not a leap year." << endl;
    }
    
return 0;
}
