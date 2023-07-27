# riscv-check
`riscv-check` is an utility that lets you analyze compiler's ability to convert specific patterns in C code to asm instructions from certain RISC-V extensions.

## Motivation
```C
#include <stdint.h>

uint64_t test(uint64_t rs1, uint64_t rs2) {
	return rs1 < rs2 ? rs2 : rs1;
}
```
E.g. `gcc` 13.1.0 converts such C code to `maxu` instruction from RISC-V `bitmanip` extension.

The goal of the project is to analyze such behavior for a number of tests and provide results to a user.

## Tests format
The repository contains tests for `bitmanip` extension in the following format: `<tests_dir>/<instruction_name>/<test_name>.c`.

Each test or group of tests can be disabled by prefixing corresponding file / dir names with `_`.

You can easily add your own tests by creating dirs and files in the format above.

## Configuration
`riscv-check` is configured via `config.json` file.

## Run
Once configured install requirements and run the application:
```bash
pip install -r requirements.txt
python3 riscv-check.py
```
Eventually check `.csv` file for results.

## Utility output example
| instruction | test    | -O   | result |
|-------------|---------|------|--------|
| add.uw      | mask    | 0    | failed |
| add.uw      | mask    | 123  | passed |
| maxu        | ternary | 0123 | passed |

## License
Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
