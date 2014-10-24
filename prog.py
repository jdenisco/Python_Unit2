#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: prog
#   date: 2014-10-24
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import argparse


parser = argparse.ArgumentParser()
parser.add_argument("square", help="displays a square of a given number",
                    type=int)
args = parser.parse_args()
print args.square**2
