#!/usr/bin/python3

from num2words import num2words

for i in range(1,101):
    if i%10 == 0:
        print(num2words(i))
    else:
        print(i)
