#include <stdint.h>

uint64_t test(uint64_t rs1, uint64_t rs2) {
	return rs1 < rs2 ? rs2 : rs1;
}
