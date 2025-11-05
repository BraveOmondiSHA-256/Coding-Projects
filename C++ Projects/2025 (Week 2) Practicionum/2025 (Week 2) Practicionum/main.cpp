/*
* Author: Brave Omondi
* Assignment Title: Hello World
* Assignment Description:
* Due Date:01/01/2025
* Date Created:01/01/2025
* Date Last Modified:01/01/2025
*/
#include <iostream>
using namespace std;

string name;
int year_born;
int days_old;
int current_age;
int current_year = 2025;

int main() {
    
    cout << "What is your name? ";
    cin >> name;
    cout << "What year were you born? ";
    cin >> year_born;
    current_age = current_year - year_born;
    days_old = current_age * 365;
    cout << "This year on your birthday, you will be " << days_old << " days old." << endl;
    
    return 0;
}
    
    

