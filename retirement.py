# -*- coding: utf-8 -*-
"""
Simple program to figure out when you can exit.
"""

# Credits
__author__ =        'George Flanagin'
__copyright__ =     'Copyright 2019 George Flanagin'
__credits__ =       'None. This idea has been around forever.'
__version__ =       '1.0'
__maintainer__ =    'George Flanagin'
__email__ =         'me@georgeflanagin.com'
__status__ =        'final.'
__license__ =       'MIT'


import typing
from   typing import *

import argparse
import datetime 
import os
import sys

import dateutil
import dateutil.parser
from   dateutil.relativedelta import relativedelta as rdelta


def retirement_main(g:argparse.Namespace) -> tuple:
    """
    hiredate     -- used for calculating years of service.
    birthday     -- to determine age
    min_age      -- gotta be old enough
    req_years    -- gotta work here a while
    magic_number -- there always is one.

    returns -- a tuple of possibly relevant info, or None if there is 
        no ability to retire.
    """       
    now = datetime.date.today()

    # Only the most cursory checking.
    if not g.birthday < g.hiredate < now: 
        print("\n".join(["you must have been born before you were hired,",
            "and you must have been hired before today."]))
        sys.exit(os.EX_DATAERR)
    
    current_age     = now - g.birthday
    current_service = now - g.hiredate

    old_enough_on   = g.birthday + rdelta(years=g.min_age)
    old_enough_now  = old_enough_on < now
    long_enough_on  = g.hiredate + rdelta(years=g.req_years)
    long_enough_now = long_enough_on < now

    if long_enough_now and old_enough_now:
        return now, 0, old_enough_on, long_enough_on, current_age.days, current_service.days
    
    no_earlier_than = max(long_enough_on, old_enough_on)
    magic_date      = now + rdelta(rdelta(years=g.magic_number) - rdelta(current_age) - rdelta(current_service))/2
    quit_on         = max(magic_date, no_earlier_than)

    if old_enough_on < g.hiredate: 
        old_enough_on = 'when you started.'
    elif old_enough_on < now: 
        old_enough_on = 'now'
    if long_enough_on < now:       
        long_enough_on = 'now'

    return quit_on, (quit_on - now).days, old_enough_on, long_enough_on, current_age.days, current_service.days


if __name__ == '__main__':
    p = argparse.ArgumentParser(description='Calculate your retirement date.')
    p.add_argument('--birthday', type=str, required=True)
    p.add_argument('--hiredate',  type=str, required=True)

    # [1] Most formulae have some magic number that is connected to
    #       the sum of years of service and age.
    # [2] And most places require you to work there for a while.
    # [3] And we don't want to retire toddlers.
    #
    # These defaults are for University of Richmond's policy in 2019.

    p.add_argument('--min-age', type=int, default=55)
    p.add_argument('--req-years', type=int, default=10)
    p.add_argument('--magic-number', type=int, default=75)

    g = p.parse_args()
    g.birthday = dateutil.parser.parse(g.birthday).date()
    g.hiredate = dateutil.parser.parse(g.hiredate).date()

    _ = retirement_main(g)
    print("""
Exit date: {} in {} days
Old enough: {}
Long enough: {}
You are now {} days old
You have been working here {} days""".format(_[0], _[1], _[2], _[3], _[4], _[5]))
