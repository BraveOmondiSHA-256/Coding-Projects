//
//  main.cpp
//  Proggramm 16- maths quiz
//
//  Created by Brave Omondi on 23/10/2025.
//

#include <iostream>
#include <cstdlib>
#include <iomanip>
using namespace std;

int calculate_score(int a, int b){
    int answer = 10 * b;
    return answer;
}

int main() {
    srand(1337);
    
    int multiA;
    int multiB;
    int finalScore;
    int keepScore = 0;
    
    cout << "Multiplication Quiz" << endl;
    cout << endl;
    cout << "This program will test how well you have memorized" << endl;
    cout << "your times tables. You will be given 10 random" << endl;
    cout << "questions.  Each question is worth ten points." << endl;
    
    for(size_t i = 1; i <= 10; ++i){
        multiA = rand() % 13;
        multiB = rand() % 13;
        int userAnswer;
        cout << endl;
        cout << setw(2) << i << ": " << multiA << " x " << multiB << " = ";
        cin >> userAnswer;
        int correctAnswer = multiA * multiB;
        if(userAnswer == correctAnswer){
            cout << setw(6) << userAnswer << " is correct." << endl;
        }
        else{
            cout << setw(6) << userAnswer <<  " is incorrect.  The correct answer is " << correctAnswer << endl;
        }
        if(userAnswer == correctAnswer){
            keepScore++;
            finalScore = calculate_score(10, keepScore);
        }
    }
    cout << endl;
    cout << "Final score: " << finalScore << "%" << endl;
    
    return 0;
}
