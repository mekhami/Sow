#/usr/bin/env python
###################################
##  A Harvest Command Line App   ##
###################################
'''Harvest.

Usage:
    console.py [options]
    console.py add [hours] [project] [task]
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
from utils import set_credentials
from harvest import Harvest
import pprint
import json

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
today = harvest.today

if parser['add']:
    if not parser['hours']:
        hours = int(raw_input("How many hours for this entry? "))
    else:
        hours = parser['hours']
    if not parser['project']:
        for key, value in enumerate(today['projects']):
            print key + 1, value['name']
        client = today['projects'][int(raw_input("Select a project: "))-1]
        client_id = client['id']
        pprint.pprint(client)
        if not parser['task']:
            for key, task in enumerate(client['tasks']):
                print key + 1, task['name']
        task = client['tasks'][int(raw_input("Select a task: "))-1]
        task_id = task['id']
    else:
        client_id = parser['project']
        task_id = parser['task']
    if not parser['note']:
        note = raw_input("Leave a note (optional): ")
    else:
        note = parser['note']

    data = {"notes": note, "project_id":client_id, "hours":hours, "task_id":task_id}
    harvest.add(data)    
