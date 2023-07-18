#include <stdint.h>

uint64_t maxu(uint64_t rs1, uint64_t rs2) {
    uint64_t rd;

    if (rs1 < rs2)
        rd = rs2;
    else
        rd = rs1;

    return rd;
}
