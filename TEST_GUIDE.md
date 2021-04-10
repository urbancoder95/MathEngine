# Testing guidlines
This document covers the testing guidelines for the c++ codebase. The development has been mostly done in Linux, although we understand users want to use it in windows as well. This comes with path changes to files for correct output file generation. This document covers the necessary steps to follow until we create a branch for windows seperately. 

## Linux
The codebase is already ready and good-to-go for testing. To run the testing script, just run the following command:- 

    g++ test_array.cc math_engine/src/array.cc -std=c++11

Then run the `a.out` as you would and see the output. 

## Windows
First install a c++ compiler. We use GNU compiler which you can get using `Cygwin` or `MinGW`. For more information on GNU compilers check [this](https://gcc.gnu.org/install/binaries.html) out.

Then run the same command as in Linux except the path to `array.cc` will use `\` instead of `/`. The rest is same. 

You can create your own test codes, but for now, the codebase only supports single dimensional integer vectors. 