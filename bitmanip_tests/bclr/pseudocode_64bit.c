#include <stdint.h>
#define xlen 32

int32_t test(int32_t rs1, int32_t rs2) {
    int32_t index = rs2 & (xlen - 1);
    int32_t rd = rs1 & ~(1 << index);
    return rd;
}
