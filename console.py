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
parser = docopt(__doc__)

config = ConfigParser.RawConfigParser()
config.read('~/.harvconfig')

if parser['add']:
    if parser['<alias>']:
        add(get_timesheet(), parser['<alias>'], parser['<hours>'], parser['<note>'])
    else:
        add(get_timesheet(), False)

#NOTES
#Submit Timesheet for Approval
#Timer Integration? Does anyone use this?
#Show Weekly Timesheet

