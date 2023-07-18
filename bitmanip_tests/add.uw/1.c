#include <stdint.h>

int64_t adduw(int64_t rs2, int64_t rs1) {
    int64_t index = rs1 & 0xFFFFFFFF;

    return rs2 + index;
}
