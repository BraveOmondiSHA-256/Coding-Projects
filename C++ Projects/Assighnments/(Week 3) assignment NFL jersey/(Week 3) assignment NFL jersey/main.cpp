/*
 * Author: Brave Omondi
 * Assignment Title: Program 6 - NFL Jersey
 * Assignment Description:
 * Due Date:
 * Date Created:
 * Date Last Modified:
 */

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    
    int number;

       cout << "Enter the number of a football jersey (1 ... 99):";
       cin >> number;

       if (number < 1 || number > 99) {
           cout << "Invalid number" << endl;
           return 0;
       }

       if (number >= 1 && number <= 19) {
           cout << "Quarterback" << endl;
           cout << "Kicker" << endl;
       }

       if ((number >= 10 && number <= 19) || (number >= 80 && number <= 89)) {
           cout << "Wide Receiver" << endl;
       }

       if (number >= 20 && number <= 49) {
           cout << "Running Back" << endl;
           cout << "Cornerback" << endl;
           cout << "Safety" << endl;
           cout << "Fullback" << endl;
       }

       if (number >= 50 && number <= 59) {
           cout << "Center" << endl;
       }

       if ((number >= 50 && number <= 59) || (number >= 90 && number <= 99)) {
           cout << "Linebacker" << endl;
       }

       if (number >= 60 && number <= 79) {
           cout << "Offensive Lineman" << endl;
       }

       if ((number >= 60 && number <= 79) || (number >= 90 && number <= 99)) {
           cout << "Defensive Lineman" << endl;
       }

       if (number >= 80 && number <= 89) {
           cout << "Tight End" << endl;
       }
    return 0;
}
