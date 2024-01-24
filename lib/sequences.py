#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        return [0]
    elif length == 1:
        return [0,1]
    else:
        x = [0,1]
        for i in range(length-2):
            last = x[-1]
            second_to_last = x[-2]
            new = last + second_to_last
            x.append(new)
        return x


print(print_fibonacci(0))
print(print_fibonacci(1))
print(print_fibonacci(5))