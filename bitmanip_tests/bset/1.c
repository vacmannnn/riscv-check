#include <stdint.h>

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t index = rs2 & 63;

    return rs1 | (1 << index);
}
