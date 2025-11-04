/*
* Author: Brave Omondi
* Assignment Title: Program 3- Seconds to Time of Day
* Assignment Description:
* Due Date:01/01/2025
* Date Created:01/01/2025
* Date Last Modified:01/01/2025
*/
#include <iostream>
#include <cmath>
using namespace std;

int main() {
   
    int timeDaySecs;
    int hours;
    int minutes;
    int minutesWhole;
    int secondsWhole;
    int seconds;

    cout << "Enter the time of day in seconds (0...86400): ";
    cin >> timeDaySecs;
    hours = timeDaySecs / 3600;
    cout << "Hours: " << hours << endl;
    minutesWhole = timeDaySecs % 3600;
    minutes = minutesWhole / 60;
    cout << "Minutes: " << minutes << endl;
    secondsWhole = minutesWhole % 60;
    seconds = secondsWhole;
    cout << "Seconds: " << seconds << endl;

    return 0;
}
    
