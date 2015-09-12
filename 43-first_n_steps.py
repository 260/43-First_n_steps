#!/usr/bin/python3

# This problem is http://yukicoder.me/problems/43

def ceil(float_number):
    int_number = int(float_number)
    if float_number > int_number:
        return int_number + 1
    return int_number

first_line = input()
a_and_b = list(map(int, first_line.split(' ')))
one_step = a_and_b[0]
interval = a_and_b[1]

print(ceil(interval/one_step))


# print(one_step, interval)
