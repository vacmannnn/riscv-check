#include <stdint.h>
#define SHAMT_IM 5

int64_t test(int64_t rs1) {
    int64_t index = SHAMT_IM & 63;

    return (rs1 >> index) & 1;
}
