//
//  main.cpp
//  Week 8 - Practicum
//
//  Created by Brave Omondi on 16/10/2025.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>


using namespace std;

string stars(int n) {
    if (n < 0) n = 0;
    
        return string (n, '*');
}

void print_hist_line(int label, int count) {
    cout << setw(2) << label  // print number right-aligned in 2 spaces
         << " | "             // print a space, a bar, and another space
         << stars(count)      // call the first function to make the stars
         << endl;             // move to a new line
}

int main() {
    
    
    string filename;
    cout << "Input filename: ";
    getline(cin, filename);
    cout << endl;
    
    ifstream inputBellCurve (filename);
    
    if(!inputBellCurve){
        cout << "Error: could not open file." << endl;
        return 1;
    }
    
    cout << "Reading from " << filename << endl;
    cout << endl;
    
    int label, count;
    
    while (inputBellCurve >> label >> count) {
            print_hist_line(label, count);  // print one line of stars
        }
    inputBellCurve.close();  // close the file when done
    return 0;
}
