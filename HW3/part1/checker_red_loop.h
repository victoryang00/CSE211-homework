#include <assert.h>
#include <stdio.h>

void check_values(double *ref, double *actual, int size) {
    printf("%lf %lf\n", ref[0], actual[0]);
    assert(ref[0] == actual[0]);
} 
