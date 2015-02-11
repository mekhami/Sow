import ConfigParser
import getpass
import keyring
import os
from harvest import Harvest
from dateutil.parser import parse
from datetime import *


def get_config():
    config = ConfigParser.RawConfigParser()
    config.read(os.path.expanduser('~/.harvconfig'))
    return config

def set_credentials():
    print '''PyHarvest needs your username and password to authenticate to Harvest.
    Your username will be stored in a config file, and password stored in your system's keyring.
    This information will not be communicated anywhere other than your file system and Harvest.'''
    username = raw_input("Username: ")
    password = getpass.getpass()
    URI = "https://" + raw_input("What is the subdomain of your Harvest application? (the 'foo' in http://foo.harvestapp.com'): ") + ".harvestapp.com"

    configdata = {'Username': username, 'URI': URI}
    config_write('Harvest', configdata)
    keyring.set_password("Harvest", username, password)

    return (URI, username, password)

def reauth(config):
    username = raw_input("Username: ")
    password = getpass.getpass()
    config.remove_option('Harvest', 'Username')
    config.set('Harvest', 'Username', username)
    with open(os.path.expanduser('~/.harvconfig'), 'wb') as configfile:
        config.write(configfile)

    try:
        keyring.delete_password('Harvest', username)
    except keyring.errors.PasswordDeleteError:
        pass
    keyring.set_password('Harvest', username, password)
    print "Harvest login information changed."

def get_credentials():
    config = get_config()
    username = config.get('Harvest', 'Username')
    password = keyring.get_password("Harvest", username)
    URI = config.get('Harvest', 'uri')

    return URI, username, password

def get_timesheet():
    try:
        URI, USERNAME, PASSWORD = get_credentials()
    except ConfigParser.NoSectionError:
        URI, USERNAME, PASSWORD = set_credentials()

    harvest = Harvest(URI, USERNAME, PASSWORD)
    return harvest 

def get_int(prompt):
    parsed = False
    while parsed == False:
        try:
            answer = int(raw_input(prompt))
            parsed = True
        except ValueError:
            print 'Invalid value!'
    return int(answer)

def config_write(section, args):
    '''Requires section name as an argument and a dictonary with name: info pairs.
    Writes to the ~/.harvconfig file.'''
    config = ConfigParser.RawConfigParser()
    config.add_section(section)
    for key, value in args.iteritems():
        config.set(section, key, value)
    with open(os.path.expanduser('~/.harvconfig'), 'ab+') as configfile:
        config.write(configfile)

def get_week():
    today = datetime.today()
    weekday = datetime.timetuple(today)[6]
    yearday = datetime.timetuple(today)[7]
    return yearday - weekday

