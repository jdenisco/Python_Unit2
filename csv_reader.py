#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
#   file: cvs_reader
#   date: 2014-10-25
#   author: jdenisco
#   email: james.denisco@genesys.com
#
# Copyright © 2014 jdenisco <james.denisco@genesys.com>
#

"""
Description:
"""

import csv
 
#----------------------------------------------------------------------
def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))
 
#----------------------------------------------------------------------
if __name__ == "__main__":
    csv_path = "TB_data_dictionary_2014-10-25.csv"
    with open(csv_path, "rb") as f_obj:
        csv_reader(f_obj)
