import math
import re
import sys
import time
import requests
from collections import Counter
import pyperclip
sys.setrecursionlimit(10**6)

try:
    import numpy as np
except ImportError as e:
    print(e)

def print_(input):
    print(input)
    pyperclip.copy(input)
