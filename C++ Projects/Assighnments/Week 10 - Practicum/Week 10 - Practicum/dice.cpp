// dice.cpp
#include <cstdlib>  // for rand(), srand()
#include <ctime>    // for time()
using namespace std;

int rollDice(int count, int sides) {
    srand(time(nullptr));  // seed random generator once per run
    int total = 0;

    for (int i = 0; i < count; i++) {
        int roll = (rand() % sides) + 1;  // gives number from 1 to sides
        total += roll;
    }

    return total;
}
