#include <stdint.h>

int64_t test(int64_t rs) {
    int64_t rd = 0;

    for (int i = 0; i < 8; i++) {
        int8_t byte = rs >> (i * 8);

        if (byte)
            (rd |= (0b11111111u << (i * 8)));
    }

    return rd;
}
