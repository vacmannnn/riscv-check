#include <stdint.h>

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t shamt = rs2 & 0b111111;
    int64_t rd = (rs1 >> shamt) | (rs2 << (64 - shamt));

    return rd;
}
