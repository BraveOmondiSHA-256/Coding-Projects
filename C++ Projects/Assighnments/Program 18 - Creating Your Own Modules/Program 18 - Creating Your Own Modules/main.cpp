//  main.cpp
//  Program 13: List of test scores (Insert & Remove version)
//
//  Author: Brave Omondi
//  Date: 05/10/2025

#include <iostream>
#include "arrayTools.h"
using namespace std;

const size_t GRADE_MAX = 10;

// prints the menu
void printMenu() {
    cout << endl;
    cout << "1. Enter scores" << endl;
    cout << "2. Print scores" << endl;
    cout << "3. Clear all scores" << endl;
    cout << "4. Insert score" << endl;
    cout << "5. Remove score" << endl;
    cout << "6. Stats" << endl;
    cout << "9. Quit" << endl;
    cout << endl;
}

// menu item 1: enter scores
void enterScores(int grades[], size_t &count, size_t max) {
    if (count >= max) {
        cout << "List of scores is full" << endl;
        return;
    }

    cout << "Enter up to " << (max - count) << " scores. Type -1 when done." << endl;

    while (count < max) {
        int score;
        if (!(cin >> score)) return; // input failure, just stop

        if (score == -1) break;

        if (score < 0) {
            cout << "Negative scores are not allowed. Try again or type -1 to stop." << endl;
            continue;
        }

        grades[count] = score;
        ++count;
    }
}

// menu item 2: print scores
void printScores(const int grades[], size_t count) {
    if (count == 0) {
        cout << "List of scores is empty" << endl;
        return;
    }
    cout << "List of scores:" << endl;
    for (size_t i = 0; i < count; ++i) {
        cout << i << ": " << grades[i] << endl;
    }
}

int main() {
    int grades[GRADE_MAX];
    size_t count = 0;    // how many scores are currently stored
    int choice;

    while (true) {
        printMenu();

        cout << "What would you like to do? ";
        cin >> choice;
        cout << endl;
        cout << "You selected " << choice << endl << endl;

        switch (choice) {
            case 1: { // Enter scores
                enterScores(grades, count, GRADE_MAX);
                break;
            }

            case 2: { // Print scores
                printScores(grades, count);
                break;
            }

            case 3: { // Clear all
                count = 0;
                cout << "All scores have been cleared" << endl;
                break;
            }

            case 4: { // Insert score
                if (count >= GRADE_MAX) {
                    cout << "List of scores is full" << endl;
                    break;
                }

                size_t pos;
                cout << "Which position would you like to insert at? ";
                cin >> pos;

                int newScore;
                cout << "Enter score to insert: ";
                cin >> newScore;

                if (newScore < 0) {
                    cout << "Negative scores are not allowed." << endl;
                    break;
                }

                int rc = arrayInsert(newScore, pos, grades, count, GRADE_MAX);
                if (rc == ERROR_MAX_SIZE) {
                    cout << "Array size limit reached." << endl;
                } else if (rc == ERROR_INVALID_POS) {
                    cout << "Invalid position" << endl;
                } else {
                    cout << endl;
                    cout << "Inserting " << newScore << " at position " << pos << "." << endl;
                }
                break;
            }

            case 5: { // Remove score
                if (count == 0) {
                    cout << "List of scores is empty" << endl;
                    break;
                }

                size_t pos;
                cout << "Which position would you like to delete? ";
                cin >> pos;

                int rc = arrayDelete(pos, grades, count);
                if (rc == ERROR_INVALID_POS) {
                    cout << "Invalid position" << endl;
                } else {
                    cout << endl;
                    cout << "Deleting score at position " << pos << "." << endl;
                }
                break;
            }

            case 6: { // Stats
                if (count == 0) {
                    cout << "List of scores is empty" << endl;
                    break;
                }
                int lo = arrayMin(grades, count);
                int hi = arrayMax(grades, count);
                int tot = arrayTotal(grades, count);
                double avg = arrayAverage(grades, count);

                cout << "Lowest score: " << lo << endl;
                cout << "Highest score: " << hi << endl;
                cout << "Total points: " << tot << endl;
                cout << "Average: " << avg << endl;
                break;
            }

            case 9: {
                cout << "Goodbye." << endl;
                return 0;
            }

            default: {
                cout << "Invalid option." << endl;
                break;
            }
        }
    }
}
