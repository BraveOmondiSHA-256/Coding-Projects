/*
 * Author: Brave Omondi
 * Assignment Title: Program 8- Quadratic formula
 * Assignment Description:
 * Due Date:01/01/2025
 * Date Created:01/01/2025
 * Date Last Modified:01/01/2025
 */

#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

int main() {
    cout << fixed << setprecision(2);

    double coefficientA, coefficientB, coefficientC;
    double discriminant;
    double root1, root2;
    double vertexX, vertexY;
    bool hasRoots = true;

    cout << "Enter 3 coefficients for a quadratic equation: ";
    cin >> coefficientA >> coefficientB >> coefficientC;
    cout << endl;

    if (coefficientA == 0) {
        cout << "NOT A PARABOLA" << endl;
        return 0;
    }

    discriminant = (coefficientB * coefficientB) - (4 * coefficientA * coefficientC);

    if (discriminant > 0) {
        root1 = (-coefficientB - sqrt(discriminant)) / (2 * coefficientA);
        root2 = (-coefficientB + sqrt(discriminant)) / (2 * coefficientA);
        if (root1 > root2) swap(root1, root2);
    }
    else if (discriminant == 0) {
        root1 = root2 = -coefficientB / (2 * coefficientA);
    }
    else {
        hasRoots = false;
    }

    vertexX = -coefficientB / (2 * coefficientA);
    vertexY = (coefficientA * vertexX * vertexX) + (coefficientB * vertexX) + coefficientC;

    if (hasRoots) {
        if (discriminant > 0) {
            cout << "Roots: " << root1 << ", " << root2 << endl;
        }
        else {
            cout << "Roots: " << root1 << endl;
        }
    }
    else {
        cout << "Roots: NO REAL ROOTS" << endl;
    }

    cout << "Vertex: (" << vertexX << ", " << vertexY << ")" << endl;

    return 0;
}



