//
//  main.cpp
//  Programme 13: test scores import
//
//  Created by Brave Omondi on 15/10/2025.
//

#include <iostream>
#include <fstream>
#include <vector>
#include <iomanip>
using namespace std;

int main() {
    string filename;
    cout << "Input filename: ";
    cin >> filename;

    ifstream inputFile(filename);

    if (!inputFile) {
        cout << "Error: could not open file." << endl;
        return 1;
    }

    cout << "Reading from " << filename << endl;

    vector<int> scores;
    int value;

    while (inputFile >> value) {
        scores.push_back(value);
    }
    inputFile.close();

    if (scores.empty()) {
        cout << "No scores found in file." << endl;
        return 0;
    }

    int total = 0;
    int highest = scores[0];
    int lowest = scores[0];

    cout << endl;

    for (size_t i = 0; i < scores.size(); ++i) {
        cout << i + 1 << ": " << scores[i] << endl;
        total += scores[i];
        if (scores[i] > highest) highest = scores[i];
        if (scores[i] < lowest) lowest = scores[i];
    }

    double average = static_cast<double>(total) / scores.size();

    cout << endl;
    cout << "Total points: " << total << endl;
    cout << "Highest score: " << highest << endl;
    cout << "Lowest score: " << lowest << endl;
    cout << "Average: " << fixed << setprecision(1) << average << endl;

    return 0;
}
