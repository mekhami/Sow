#/usr/bin/env python
###################################
##  A Harvest Command Line App   ##
###################################
'''Harvest.

Usage:
    console.py [options]
    console.py add [(<alias> <hours> <note>)]
    console.py start [project] [task]
    console.py stop <number> <note>
    console.py reauth <username> <password>
    console.py show ([today|yesterday|week] | --date <date>)

Options:
  -h --help          Show this screen.
  --version          Show the version.
'''

from docopt import docopt
from commands import add, show
from utils import get_timesheet, get_config


# NOTES
# Submit Timesheet for Approval
# Timer Integration? Does anyone use this?
# Show Weekly Timesheet

def main(args, config, timesheet):
    if args['add']:
        add(args, config, timesheet)
    if args['show']:
        show(args, timesheet)

if __name__ == '__main__':
    args = docopt(__doc__)
    config = get_config() 
    timesheet = get_timesheet()
    main(args, config, timesheet)

