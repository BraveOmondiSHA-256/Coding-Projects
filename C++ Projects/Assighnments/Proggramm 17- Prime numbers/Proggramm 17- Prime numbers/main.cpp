//
//  main.cpp
//  Proggramm 17- Prime numbers
//
//  Created by Brave Omondi on 29/10/2025.
//

#include <iostream>
#include <cmath>
using namespace std;

// Function to check if a number is prime
bool isPrime(int n) {
    if (n < 2) {
        return false;
    }

    for (int i = 2; i <= sqrt(n); i++) {
        if (n % i == 0) {
            return false;   // not prime
        }
    }

    return true;  // prime
}

int main() {
    int maxNum;

    cout << "Enter a max number: ";
    cin >> maxNum;

    cout << "The prime numbers less than or equal to " << maxNum << " are: " << endl;

    // Loop through all numbers and print primes
    for (int i = 2; i <= maxNum; i++) {
        if (isPrime(i)) {
            cout << i << ", ";
        }
    }
    cout << endl;
    return 0;
}
