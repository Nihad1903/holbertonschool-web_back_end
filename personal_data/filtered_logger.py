#!/usr/bin/env python3
'''Filtered Logger File'''
import re

def filter_datum(fields: list, redaction: str, message: str, separator: str) -> str:
    '''Filtered Datum Function'''
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*', lambda m: f"{m.group(1)}={redaction}", message)