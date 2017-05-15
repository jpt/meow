#!/usr/bin/python

all_letters = ["@a-h","@i-p","@q-x","@y-z","@A-H","@I-P","@Q-X"]

template = '''
lookup meow_{number} useExtension {{
    sub {one} {two} {three} {four} by m_e_o_w.liga;
}} meow_{number};
'''
number = 0
lookup_string = ''

for one in all_letters:
    for two in all_letters:
        for three in all_letters:
            for four in all_letters:
                lookup_string += template.format(number=number, one=one, two=two, three=three, four=four)
                number += 1
print(lookup_string)