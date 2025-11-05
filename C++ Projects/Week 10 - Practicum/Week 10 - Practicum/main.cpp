// main.cpp
#include <iostream>
using namespace std;

// function prototype (so main knows it exists)
int rollDice(int count, int sides);

int main() {
    int numDice, numSides;

    while (true) {
        cout << "How many dice to roll (0 to quit)? ";
        cin >> numDice;

        if (numDice == 0) {
            cout << "\nGoodbye.\n";
            break;
        }

        cout << "How many sides? ";
        cin >> numSides;

        int result = rollDice(numDice, numSides);
        cout << "\nYour " << numDice << "d" << numSides << " roll is: " << result << "\n\n";
    }

    return 0;
}
