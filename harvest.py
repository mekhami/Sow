#!/usr/bin/env python
###################################
##  A Harvest Command Line App   ##
###################################
'''Harvest.

Usage:
    harvest.py [options]
    harvest.py track <hours> [project] [subcategory]
    harvest.py start [project] [subcategory]
    harvest.py stop <number>
    harvest.py reauth <username> <password>
    harvest.py note <comment>

Options:
  -h --help          Show this screen.
  --version          Show the version.
'''

from docopt import docopt
import ConfigParser
from utils import set_credentials
from harvest import Harvest
import pprint

parser = docopt(__doc__)

config = ConfigParser.RawConfigParser()
config.read('.harvconfig')

try:
    USERNAME = config.get('Harvest', 'Username')
    PASSWORD = config.get('Harvest', 'Password')
    URI = config.get('Harvest', 'URI')
except:
    URI, USERNAME, PASSWORD = set_credentials()

harvest = Harvest(URI, USERNAME, PASSWORD)
print harvest.status
pprint.pprint(harvest.today)


