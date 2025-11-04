#include <iostream>
using namespace std;

void printFactors(int num) {
    bool first = true;

    cout << "The factors of " << num << " are:" << endl;

    for (int i = 2; i <= num / i; i++) {
        if (num % i == 0) {
            if (!first) cout << ", ";
            cout << i;
            if (num / i != i) cout << ", " << num / i;
            first = false;
        }
    }

    if (first) {
        cout << num << " is prime";
    }

    cout << endl;
}

int main() {
    int num;

    while (true) {
        cout << "\nEnter a positive integer, or 0 to quit: ";
        cin >> num;
        cout << endl;

        if (num == 0) {
            cout << "Goodbye." << endl;
            break;
        }
        else if (num < 2) {
            cout << "Your number must be greater than 1." << endl;
        }
        else {
            printFactors(num);
        }
    }

    return 0;
}
