#!/usr/bin/env python3
""" Filtered Logger """
import re
from typing import List
import logging


def filter_datum(fields: List[str], redaction: str,
                 message: str, seperator: str) -> str:
    """ Filter sensitive data from a log message. """
    return re.sub(fr"({'.?|'.join(fields)}.?)(.*?)({seperator})",
                  lambda m: f"{m.group(1)}{redaction}{m.group(3)}", message)
