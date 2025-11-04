//
//  main.cpp
//  Program 11 (magic ball)
//
//  Created by Brave Omondi on 01/10/2025.
//

#include <iostream>
#include <string>
#include <cstdlib>

using namespace std;

const int NUM_RESPONSES = 20;

int main() {
    srand(14387);

    string responses[NUM_RESPONSES] = {
        "It is certain.",
        "It is decidedly so.",
        "Without a doubt.",
        "Yes, definitely.",
        "You may rely on it.",
        "As I see it, yes.",
        "Most likely.",
        "Outlook good.",
        "Yes.",
        "Signs point to yes.",
        "Don't count on it.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Very doubtful.",
        "Reply hazy, try again.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again."
    };

    cout << "   -= Magic 8-ball =-" << endl << endl;
    cout << "You can ask the magic 8-ball any question that has" << endl;
    cout << "a yes-no answer.  Type \"quit\" to end." << endl << endl;
    cout << "What would you like to know?" << endl << endl;

    string question;
    while (true) {
        if (!getline(cin, question)) {
            cout << "  Goodbye!" << endl;
            break;
        }

        if (question == "quit") {
            cout << "  Goodbye!" << endl;
            break;
        }

        int idx = rand() % NUM_RESPONSES;
        cout << "  " << responses[idx] << endl << endl;
    }

    return 0;
}
