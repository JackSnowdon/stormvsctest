import math
import os
import sys

import requests

print(sys.version)


def hello(name):
    return f'Hello {name}'


print(hello('Jack'))

r = requests.get('https://jacksnowdon.co.uk')

print(r.status_code)
