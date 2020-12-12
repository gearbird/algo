# Prerequisite

Python 3.7+

C++ compiler that supports C++17

VSCode with Python & C/C++ extension is recommended for debugging

## Linux Debian
```bash
sudo apt update
sudo apt install build-essential gdb
sudo apt install python
```

## Mac OS
```bash
xcode-select --install
brew install python
```
Install CodeLLDB in VSCode

# How to Code
## LeetCode

### Python Solutions
Add solution Python file as ```pyleet/[0-9]{4}.py```

### C++ Solutions
Add solution c++ file as ```leetcode/[0-9]{4}.cpp```

Boilerplate code:
```cpp
#include "common.hpp"

namespace leetcode {
    using namespace utilities;
    // solution
}

int main() {
    using namespace leetcode;
    // test code
}
```

# Build & Run

### Python
Just run Python file in pyleet

### C++
Take Leetcode #1 as example:
```bash
make
bin/0001
```

# Debug C++ in VSCode
## GDB
Select "GDB: Debug leetcode active file" in debug options

## LLDB
Select "LLDB: Debug leetcode active file" in debug options

# Other Commands for C++
## Call help for Makefile
```bash
make help
```

## Check all project related files in project
```bash
make check
```

## Clean up binary files
```bash
make clean
```
