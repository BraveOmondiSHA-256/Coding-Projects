/*
 * Author: Brave Omondi
 * Assignment Title: Program 5- Average grade calculator
 * Assignment Description:
 * Due Date:01/01/2025
 * Date Created:01/01/2025
 * Date Last Modified:01/01/2025
 */

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    
    double score1, score2, score3, score4, score5;
    double averageScore;
    
    
    cout << "Enter 5 grades; ";
    cin >>  score1 >> score2 >> score3 >> score4 >> score5;
   
    averageScore = (score1 + score2 + score3 + score4 + score5)/5.0;
    cout << "Average score: " << averageScore << endl;
    
    char finalGrade;
    if(averageScore >= 90){
        finalGrade = 'A';
    }
    else if(averageScore >= 80){
        finalGrade = 'B';
    }
    else if(averageScore >= 70){
        finalGrade = 'C';
    }
    else if(averageScore >= 60){
        finalGrade = 'D';
    }
    else{
        finalGrade = 'F';
    }
    cout << "Final grade: " << finalGrade << endl;
    return 0;
}

