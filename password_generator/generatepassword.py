#!/usr/bin/env python

import argparse
import random
import string

parser = argparse.ArgumentParser(description="Generate a password.")
parser.add_argument("-l", "--length", type=int, help="Length of password.")
args = parser.parse_args()

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*()"
    password = "".join(random.choice(characters) for _ in range(length))
    return password

if args.length:
    if args.length < 12:
        print("Password length cannot be less than 12.")
    elif args.length > 40:
        print("Password length cannot exceed 40.")
    else:
        password = generate_password(args.length)
        print(password)
else:
    password = generate_password(12)
    print(password)
