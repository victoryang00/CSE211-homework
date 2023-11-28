#include <assert.h>

void check_values(double *ref, double *actual, int size) {
    assert(ref[0] == actual[0]);
} 
