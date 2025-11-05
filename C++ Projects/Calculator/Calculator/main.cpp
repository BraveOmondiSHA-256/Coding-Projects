/*
 * Author: Brave
 * Assignment Title: Programme 2 build table
 * Assignment Description: Print table
 * Due Date: 01/01/2025
 * Date Created: 01/01/2025
 * Date Last Modified: 01/01/2025
 */
#include <iostream>
using namespace std;

int main() {
    int chosenNumberA;
    int chosenNumberB;
    int chosenOperation;
    
    cout << "Enter two numbers: ";
    cin >> chosenNumberA >> chosenNumberB;
    
    cout << "Options:" << endl;
    cout << "1. Addition" << endl;
    cout << "2. Subtraction" << endl;
    cout << "3. Multiplication" << endl;
    cout << "4. Division" << endl;
    
    cout << "Which operation do you wish to perform (1-4)? ";
    cin >> chosenOperation;
    cout << endl;
    
    switch(chosenOperation){
        case 1:
            cout << chosenNumberA << " + " << chosenNumberB << " = " <<
            (chosenNumberA + chosenNumberB) << endl;
            break;
        case 2:
            cout << chosenNumberA << " - " << chosenNumberB << " = " <<
            (chosenNumberA - chosenNumberB) << endl;
            break;
        case 3:
            cout << chosenNumberA << " * " << chosenNumberB << " = " <<
            (chosenNumberA * chosenNumberB) << endl;
            break;
        case 4:
            if (chosenNumberB > 0){
                cout << chosenNumberA << " / " << chosenNumberB << " = " <<
                (chosenNumberA / chosenNumberB) << endl;
            }
            else if (chosenNumberB == 0){
                cout << "Division by zero" << endl;
                break;
            default:
                cout << "Invalid option" << endl;
            }
    }
    return 0;
}
