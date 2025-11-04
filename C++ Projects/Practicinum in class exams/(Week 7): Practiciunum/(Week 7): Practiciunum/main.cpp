
//
// main.cpp
// (Week 6) Practiciunum
//
// Created by Brave Omondi on 02/10/2025.
//
#include <iostream>
#include <string>
using namespace std;
int main() {
const int MAX_NAMES = 10;
string names[MAX_NAMES];
int count = 0;
cout << "Enter a list of names. Type a period when you're done." << endl;
for (int i = 0; i < MAX_NAMES; i++) {
    string input;
    cin >> input;
    if (input == ".") {
        break;
    }
    names[count] = input;
    count++;
   
}
cout << endl;
    
for (int i = 0; i < count / 2; i++) {
    string temp = names[i];
    names[i] = names[count - 1 - i];
    names[count - 1 - i] = temp;
}
cout << "Reverse order:" << endl;

for (int i = 0; i < count; i++) {
    cout << i << ": " << names[i] << endl;
}

    return 0;
}
