#include <stdint.h>

int64_t test(int64_t rs) {
    int rd;
    for (rd = 0; rs != 0; rd++)
      rs = rs & (rs - 1);
    return rd;
}
