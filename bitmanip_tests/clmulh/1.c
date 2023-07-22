#include <stdint.h>

int64_t test(int64_t rs1, int64_t rs2) {
    int64_t output = 0;

    for (int i = 1; i <= 64; i++)
        if ((rs2 >> i) & 1)
            output = output ^ (rs1 >> (64 - i));

    return output;
}
