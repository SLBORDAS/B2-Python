#!/usr/bin/python36

import re

numb1 = input('numéros 1 ?')
pattern1 = re.compile('[0-9]+')
numb2 = input('numéros 2 ?')
pattern2 = re.compile('[0-9]+')

while not pattern1.match(numb1):
  numb1 = input('numéros 1 ?')

while not pattern2.match(numb2):
  numb2 = input('numéros 2 ?')

inumb1 = int(numb1)
inumb2 = int(numb2)

def add(inumb1, inumb2):
  return inumb1 + inumb2

print(add(inumb1, inumb2))
