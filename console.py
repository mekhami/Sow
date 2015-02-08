#/usr/bin/env python
###################################
##  A Harvest Command Line App   ##
###################################
'''Harvest.

Usage:
    console.py [options]
    console.py add [(<alias> <hours> <note>)]
    console.py start [project] [task]
    console.py stop <number>
    console.py reauth <username> <password>
    console.py note <comment>

Options:
  -h --help          Show this screen.
  --version          Show the version.
'''

from docopt import docopt
import ConfigParser
from utils import set_credentials, get_credentials, get_timesheet
from harvest import Harvest
from commands import add
from utils import get_timesheet, get_config
import os

#NOTES
#Submit Timesheet for Approval
#Timer Integration? Does anyone use this?
#Show Weekly Timesheet
def main(args, config, timesheet):
     if args['add']:
         add(args, config, timesheet)
         
if __name__ == '__main__':
    args = docopt(__doc__)
    config = get_config() 
    timesheet = get_timesheet(config)
    main(args, config, timesheet)

