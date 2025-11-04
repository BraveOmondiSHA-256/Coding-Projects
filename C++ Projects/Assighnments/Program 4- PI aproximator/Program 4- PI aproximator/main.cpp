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
    double piAprox1;
    double piAprox2;

    piAprox1 = 4 * ( 1.0 - (1.0/3.0) + (1.0/5.0) - (1.0/7.0) +
                    (1.0/9.0) - (1.0/11.0) );
    piAprox2 = 4 * ( 1.0 - (1.0/3.0) + (1.0/5.0) - (1.0/7.0) +
                    (1.0/9.0) - (1.0/11.0) + (1.0/13.0) );

    cout << "PI = " << piAprox1 << endl;
    cout << "PI = " << piAprox2 << endl;

    return 0;
}
