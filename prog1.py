#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: prog1
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
parser.add_argument("--verbosity", help="increase output verbosity",
                    action="store_true")
args = parser.parse_args()
if args.verbosity:
    print "Verbosity turned on"

