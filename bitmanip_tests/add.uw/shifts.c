#include <stdint.h>

int64_t test(int64_t a, int64_t b) {
    int64_t c = (b << 32) >> 32;
    return a + c;
}
