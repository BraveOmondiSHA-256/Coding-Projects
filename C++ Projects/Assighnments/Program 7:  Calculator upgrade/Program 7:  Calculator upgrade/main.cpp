/*
 * Author: Brave Omondi
 * Assignment Title: Program 7- Average grade calculator
 * Assignment Description:
 * Due Date:01/01/2025
 * Date Created:01/01/2025
 * Date Last Modified:01/01/2025
 */

#include <iostream>
#include <cmath>
#include <algorithm>
using namespace std;

int main() {
    
    double score1, score2, score3, score4, score5;
    cout << "Enter 5 grades: ";
    cin >> score1 >> score2 >> score3 >> score4 >> score5;

    
    int average = (score1 + score2 + score3 + score4 + score5) / 5.0;
    int highest = max({score1, score2, score3, score4, score5});
    int lowest  = min({score1, score2, score3, score4, score5});
    int invalid =
    (score1 < 0) || (score1 > 100) ? score1 :
    (score2 < 0) || (score2 > 100) ? score2 :
    (score3 < 0) || (score3 > 100) ? score3 :
    (score4 < 0) || (score4 > 100) ? score4 :
    (score5 < 0) || (score5 > 100) ? score5 : 0;
    
   
    
    
    char grade;
    if (average >= 90) {
        grade = 'A';
    }
    else if (average >= 80) {
        grade = 'B';
    }
    else if (average >= 70) {
        grade = 'C';
    }
    else if (average >= 60) {
        grade = 'D';
    }
    else {
        grade = 'F';
    }

    if( (score1 >= 0 && score1 <= 100) &&
        (score2 >= 0 && score2 <= 100) &&
        (score3 >= 0 && score3 <= 100) &&
        (score4 >= 0 && score4 <= 100) &&
        (score5 >= 0 && score5 <= 100) ) {
        cout << "Average score: " << average << endl;
        cout << "Final grade: " << grade << endl;
        cout << "Highest score: " << highest << endl;
        cout << "Lowest score: " << lowest << endl;
    }
    else{
        cout << "Invalid score: " << invalid << endl;
           
       }

    return 0;
}
