#include <assert.h>

void check_values(float *ref, float *actual, int size) {
    for (int i = 0; i < size; i++)
        assert(ref[i] == actual[i]);
} 
