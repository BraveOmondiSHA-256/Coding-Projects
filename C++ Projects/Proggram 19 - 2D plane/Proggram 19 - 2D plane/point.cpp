

//  point.cpp
//  Proggram 19 - 2D plane
//
//  Created by Brave Omondi on 05/11/2025.
//

#include "point.h"
#include <cmath>

Point::Point(){
    x = 0;
    y = 0;
}

Point::Point(double xValue, double yValue){
    x = xValue;
    y = yValue;
}

Point::Point(double xyValue){
    x = xyValue;
    y = xyValue;
}
double Point::getX(){
    return x;
}
double Point::getY(){
    return y;
}
void Point::moveTo(double newX, double newY){
    x = newX;
    y = newY;
}
void Point::moveBy(double xOffset, double yOffset){
    x = x + xOffset;
    y = y + yOffset;
}
void Point::scaleBy(double scaleFactor){
    x = x * scaleFactor;
    y = y * scaleFactor;
}
double Point::distanceBetween(Point &other){
    double distanceX = x - other.x;
    double distanceY = y - other.y;
    return std::sqrt(distanceX * distanceX + distanceY * distanceY);
}
