//
//  anyTools.cpp
//  Program 18 - Creating Your Own Modules
//
//  Created by Brave Omondi on 02/11/2025.
//
#include "arrayTools.h"

int arrayInsert(int value, size_t position, int data[], size_t &count, size_t max) {
    if (count >= max) return ERROR_MAX_SIZE;
    if (position > count) return ERROR_INVALID_POS;

    // shift right to make room
    for (size_t i = count; i > position; --i) {
        data[i] = data[i - 1];
    }
    data[position] = value;
    ++count;
    return SUCCESS;
}

int arrayDelete(size_t position, int data[], size_t &count) {
    if (position >= count) return ERROR_INVALID_POS;

    // shift left to remove
    for (size_t i = position; i + 1 < count; ++i) {
        data[i] = data[i + 1];
    }
    --count;
    return SUCCESS;
}

int arrayMin(int data[], size_t count) {
    // caller should ensure count > 0
    int m = data[0];
    for (size_t i = 1; i < count; ++i) {
        if (data[i] < m) m = data[i];
    }
    return m;
}

int arrayMax(int data[], size_t count) {
    // caller should ensure count > 0
    int m = data[0];
    for (size_t i = 1; i < count; ++i) {
        if (data[i] > m) m = data[i];
    }
    return m;
}

int arrayTotal(int data[], size_t count) {
    int sum = 0;
    for (size_t i = 0; i < count; ++i) sum += data[i];
    return sum;
}

double arrayAverage(int data[], size_t count) {
    if (count == 0) return 0.0;
    return static_cast<double>(arrayTotal(data, count)) / static_cast<double>(count);
}
