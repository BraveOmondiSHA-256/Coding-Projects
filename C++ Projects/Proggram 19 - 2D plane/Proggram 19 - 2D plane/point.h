#pragma once
//  point.h
//  Proggram 19 - 2D plane
//
//  Created by Brave Omondi on 05/11/2025.
//

#include<iostream>
using namespace std;

class Point{
    
private:
    double x;
    double y;

public:
    Point();
    Point(double xValue, double yValue);
    Point(double xyValue);
    
    double getX();
    double getY();
    void moveTo(double newX, double newY);
    double distanceBetween(Point &other);
    void moveBy(double xOffset, double yOffset);
    void scaleBy(double scaleFactor);

};
