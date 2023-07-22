#include <stdint.h>
#define xlen 64

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t index = rs2 & (xlen - 1);
    int64_t rd = rs1 & ~(1 << index);
    return rd;
}
