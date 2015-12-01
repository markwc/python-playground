#!/usr/bin/python3

while True:
    print('Enter command string: ')
    command_string = input()
    if '' == command_string:
        break
    arguments = command_string.split()
    if ('test1' == arguments[0]):
        for arg in arguments:
            print(arg)
    else:
        print(arguments[0] + ': command not found')
        print(arguments[0] + '  try test1')
