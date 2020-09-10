#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "marcornett"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description='Perform transformation on input text.')
    parser.add_argument(
        'text', help='text to be manipulated', nargs=1)
    parser.add_argument(
        '-u', '--upper', help='convert text to uppercase', action='store_true')
    parser.add_argument(
        '-l', '--lower', help='convert text to lowercase', action='store_true')
    parser.add_argument(
        '-t', '--title', help='convert text to titlecase', action='store_true')
    return parser


def main(args):
    """Implementation of echo"""

    # arguments
    parser = create_parser()
    namespace = parser.parse_args(args)

    if not namespace:
        parser.print_usage()
        sys.exit(1)
    text = namespace.text[0]
    lower = namespace.lower
    title = namespace.title
    upper = namespace.upper

    output = text
    if upper:
        output = output.upper()
        # print(text.upper())
    if lower:
        output = output.lower()
        # print(text.lower())
    if title:
        output = output.title()
        # print(text.title())

    print(output)


if __name__ == '__main__':
    main(sys.argv[1:])
