//
//  main.cpp
//  Progggrame 12: List of test scores
//
//  Created by Brave Omondi on 05/10/2025.
//

#include <iostream>
#include <cmath>
#include <cctype>
#include <string>
using namespace std;

int main() {
    string userNumSelect;
    const int maxCapacity = 10;
    int userListScores[maxCapacity];
    
    while(true){
        
        cout << "1. Enter scores" << endl;
        cout << "2. Print scores" << endl;
        cout << "3. Clear all scores" << endl;
        cout << "9. Quit" << endl;
        cout << endl;
        cout << "What would you like to do? ";
        cin >> userNumSelect;
        cout << endl;
        cout << "You selected " << userNumSelect << endl;
        cout << endl;
        
        int userNumSelectInt = stoi(userNumSelect);
        
        if(userNumSelectInt == 9){
            cout << "Googbye." << endl;
            break;
        }
        /*if(userNumSelectInt != 1 || 2 || 3 || 4){
            cout << "Invalid option." << endl;
            break;
        }*/
        if(userNumSelectInt == 1){
            for(int i = 0; i < maxCapacity; i++){
                cout << "Enter up to 10 scores.  Type -1 when done." << endl;
                cin >> userListScores[i];
            }
        }
    }
    
    
    return 0;
}
