//
//  anyTools.h
//  Program 18 - Creating Your Own Modules
//
//  Created by Brave Omondi on 02/11/2025.
//
#pragma once
#include <cstddef>  // defines size_t

const int SUCCESS = 0;
const int ERROR_MAX_SIZE = 1;
const int ERROR_INVALID_POS = 2;

int arrayInsert(int value, size_t position, int data[], size_t &count, size_t max);

int arrayDelete(size_t position, int data[], size_t &count);

int arrayMin(int data[], size_t count);

int arrayMax(int data[], size_t count);

int arrayTotal(int data[], size_t count);

double arrayAverage(int data[], size_t count);
