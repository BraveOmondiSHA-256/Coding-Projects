//
//  main.cpp
//  Proggram 10 password tester
//
//  Created by Brave Omondi on 29/09/2025.
//

#include <iostream>
#include <cctype>
#include <string>
using namespace std;

int main() {
    cout << "Your password must be :" << endl;
    cout << "  * At least ten characters long" << endl;
    cout << "  * Contain at least one capital letter" << endl;
    cout << "  * Contain at least one number" << endl;
    cout << "  * Contain at least one punctuation character or symbol" << endl << endl;

    string password;

    while (true) {
        cout << "Enter a password: ";
        cin >> password;

        if (password == "quit") {
            break;
        }

        cout << endl << "You typed: " << password << endl << endl;

        bool longEnough = password.length() >= 10;
        bool hasUpper = false;
        bool hasDigit = false;
        bool hasSymbol = false;

        for (size_t i = 0; i < password.length(); i++) {
            char ch = password[i];
            if (isupper(ch)) hasUpper = true;
            if (isdigit(ch)) hasDigit = true;
            if (!isalnum(ch)) hasSymbol = true;
        }
        
        if (longEnough && hasUpper && hasDigit && hasSymbol) {
            cout << "Your password is good!" << endl << endl;
        } else {
            cout << "Your password does not meet all the requirements:" << endl;
            if (!longEnough)
                cout << "  * At least ten characters long" << endl;
            if (!hasDigit)
                cout << "  * Must have at least one digit" << endl;
            if (!hasUpper)
                cout << "  * Must have at least one uppercase letter" << endl;
            if (!hasSymbol)
                cout << "  * Must have at least one symbol" << endl;
            cout << endl;
        }
    }

    return 0;
}
