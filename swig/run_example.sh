#!/bin/bash

swig -python example.i
gcc -c example.c example_wrap.c -I/usr/include/python2.7/
ld -shared example.o example_wrap.o -o _example.so
./do_example.py
rm *.so example_wrap.* example.o example.py example.pyc 

