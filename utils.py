import os
import sys
import re

def string_to_list(string):
    if isinstance(string, str):
        string = re.findall(r'\d+', string)
        string = list(map(int, string))
        return string
    elif isinstance(string, list):
        print(f'{string} is list, no need to change')
        return string
