#include <stdint.h>
#define xlen 64

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t shamt = rs2 & 0b111111;
    int64_t res = (rs1 << shamt) | (rs2 >> (xlen - shamt));
    int64_t rd = res;
    return rd;
}
