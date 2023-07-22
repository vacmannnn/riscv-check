#include <stdint.h>
#define xlen 32

int32_t test(int32_t rs1, int32_t rs2) {
    int32_t shamt = rs2 & 0b11111;
    int32_t res = (rs1 << shamt) | (rs2 >> (xlen - shamt));
    int32_t rd = res;
    return rd;
}
