#include <stdint.h>

int64_t test(int64_t rs) {
    int64_t rd = 0;
    for (int i = 31; i >= 0; i--) {
        if ((rs >> i) & 1)
            break;
        rd++;
    }
    return rd;
}
