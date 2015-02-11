#/usr/bin/env python

###################################
##  A Harvest Command Line App   ##
###################################

'''Harvest.

Usage:
    console.py [options]
    console.py add [(<alias> <hours> <note>)] [-d|--date <date>]
    console.py show ([today|yesterday|week] | --date <date>)
    console.py reauth
    console.py delete [-a|--all] [(-d|--date <date>)]

Options:
  -h --help          Show this screen.
  --version          Show the version.
'''

from docopt import docopt
from commands import add, show, delete
from utils import get_timesheet, get_config, reauth

def _main(args, config, timesheet):
    if args['add']:
        add(args, config, timesheet)
    if args['show']:
        show(args, timesheet)
    if args['reauth']:
        reauth(config)
    if args['delete']:
        delete(args, timesheet)

def main():
    args = docopt(__doc__)
    config = get_config() 
    timesheet = get_timesheet()
    _main(args, config, timesheet)

