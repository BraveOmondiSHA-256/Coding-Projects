//
// main.cpp
// Program 9: Guess the Secret Number
//
// Created by Brave Omondi on 24/09/2025.
//

#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(static_cast<unsigned int>(time(0)));

    int secretNumber = rand() % 100 + 1;
    int guess;
    int totalGuesses = 5;

    cout << "I'm thinking of a number between 1 and 100. You have five chances to guess correctly." << endl << endl;

    for (int tries = totalGuesses; tries > 0; tries--) {
        cout << "Enter your guess: ";
        cin >> guess;

        if (guess == secretNumber) {
            cout << "That is correct! You win!" << endl;
            return 0;
        }

        if (tries > 1) {
            if (guess > secretNumber) {
                if (tries == 2)
                    cout << "That's too high. This is your last guess." << endl << endl;
                else
                    cout << "That's too high. You have " << tries - 1 << " tries left." << endl << endl;
            } else {
                if (tries == 2)
                    cout << "That's too low. This is your last guess." << endl << endl;
                else
                    cout << "That's too low. You have " << tries - 1 << " tries left." << endl << endl;
            }
        } else {
            cout << "The number was " << secretNumber << ". You lose." << endl;
        }
    }

    return 0;
}
