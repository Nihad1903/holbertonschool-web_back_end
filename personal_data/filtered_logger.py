#!/usr/bin/env python3
'''Filtered Logger File'''
import re
from typing import List

def filter_datum(fields: List[str], redaction: str, message: str, separator: str) -> str:
    '''Filtered Datum Function'''
    return re.sub(r'(' + '|'.join(fields) + r')=[^' + separator + r']*', lambda m: f"{m.group(1)}={redaction}", message)
