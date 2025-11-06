//
//  main.cpp
//  Proggram 19 - 2D plane
//
//  Created by Brave Omondi on 05/11/2025.
//

#include <iostream>
#include <cassert>
#include "point.h"

using namespace std;

int main() {
  Point a;

  assert(a.getX() == 0 && "Default ctor inits x to 0");
  assert(a.getY() == 0 && "Default ctor inits y to 0");

  Point b(3, 4);
  assert(b.getX() == 3 && "Coord ctor inits x to 3");
  assert(b.getY() == 4 && "Coord ctor inits y to 4");

  a.moveTo(9, 12);
  assert(a.getX() == 9 && "a.moveTo(9, 12) sets x to 9");
  assert(a.getY() == 12 && "a.moveTo(9, 12) sets y to 12");

  a.moveBy(-3, -4);
  assert(a.getX() == 6 && "a.moveBy(-3,-4) moves x to 6");
  assert(a.getY() == 8 && "a.moveBy(-3,-4) sets y to 8");

  double distance = a.distanceBetween(b);
  assert(distance == 5.0 && "a.distanceBetween(b) and is 5");
    
  a.scaleBy(0.5);
  assert(a.getX() == 3 && "a.scaleBy(0.5) reduces x to 3");
  assert(a.getY() == 4 && "a.scaleBy(0.5) reduces y to 4");

  return(0);
}
