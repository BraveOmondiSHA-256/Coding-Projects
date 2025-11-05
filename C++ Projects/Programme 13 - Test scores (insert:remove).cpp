//  main.cpp
//  Program 13: List of test scores (Insert & Remove version)
//
//  Author: Brave Omondi
//  Date: 05/10/2025

#include <iostream>
using namespace std;

const int GRADE_MAX = 10;

int main() {
    int grades[GRADE_MAX];
    int count = 0;     // how many scores are currently stored
    int choice;

    while (true) {
        cout << endl;
        cout << "1. Enter scores" << endl;
        cout << "2. Print scores" << endl;
        cout << "3. Clear all scores" << endl;
        cout << "4. Insert score" << endl;
        cout << "5. Remove score" << endl;
        cout << "9. Quit" << endl;
        cout << endl;

        cout << "What would you like to do? ";
        cin >> choice;
        cout << endl;
        cout << "You selected " << choice << endl << endl;

        switch (choice) {
            case 1: {  // Enter scores
                if (count >= GRADE_MAX) {
                    cout << "List of scores is full" << endl;
                    break;
                }

                cout << "Enter up to " << (GRADE_MAX - count)
                     << " scores. Type -1 when done." << endl;

                while (count < GRADE_MAX) {
                    int score;
                    cin >> score;

                    if (score == -1)
                        break;

                    if (score < 0) {
                        cout << "Negative scores are not allowed. Try again or type -1 to stop." << endl;
                        continue;
                    }

                    grades[count] = score;
                    count++;
                }
                break;
            }

            case 2: {  // Print scores
                if (count == 0) {
                    cout << "List of scores is empty" << endl;
                } else {
                    cout << "List of scores:" << endl;
                    for (int i = 0; i < count; i++) {
                        cout << i << ": " << grades[i] << endl;
                    }
                }
                break;
            }

            case 3: {  // Clear all
                count = 0;
                cout << "All scores have been cleared" << endl;
                break;
            }

            case 4: {  // Insert score
                if (count >= GRADE_MAX) {
                    cout << "List of scores is full" << endl;
                    break;
                }

                int pos;
                cout << "Which position would you like to insert at? ";
                cin >> pos;

                // valid positions are 0 to count (append allowed)
                if (pos < 0 || pos > count) {
                    cout << "Invalid position: " << pos << endl;
                    break;
                }

                int newScore;
                cout << "Enter score to insert: ";
                cin >> newScore;

                if (newScore < 0) {
                    cout << "Negative scores are not allowed." << endl;
                    break;
                }

                // shift elements to the right
                for (int i = count; i > pos; i--) {
                    grades[i] = grades[i - 1];
                }

                grades[pos] = newScore;
                count++;

                cout << endl;
                cout << "Inserting " << newScore << " at position " << pos << "." << endl;
                break;
            }

            case 5: {  // Remove score
                if (count == 0) {
                    cout << "List of scores is empty" << endl;
                    break;
                }

                int pos;
                cout << "Which position would you like to delete? ";
                cin >> pos;

                // valid remove positions are 0 to count - 1
                if (pos < 0 || pos >= count) {
                    cout << "Invalid position: " << pos << endl;
                    break;
                }

                cout << endl;
                cout << "Deleting score at position " << pos << "." << endl;

                // shift left to remove element
                for (int i = pos; i < count - 1; i++) {
                    grades[i] = grades[i + 1];
                }

                count--;
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
        }  // end switch
    }      // end while

    return 0;
}
